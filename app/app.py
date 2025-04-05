import os
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import msal
from app_config import CLIENT_ID, CLIENT_SECRET, AUTHORITY, REDIRECT_PATH, SCOPE

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.urandom(24)
Session(app)

# Define roles and access control
ROLES = {
    "Admin": ["groups", "profile"],
    "User": ["profile"],
}

def has_access(role, page):
    return page in ROLES.get(role, [])

@app.route("/")
def index():
    if not session.get("user"):
        session["flow"] = _build_auth_code_flow(scopes=SCOPE)
        return render_template("index.html", auth_url=session["flow"]["auth_uri"])
    return render_template("index.html", user=session["user"])

@app.route("/login")
def login():
    session["flow"] = _build_auth_code_flow(scopes=SCOPE)
    return redirect(session["flow"]["auth_uri"])

@app.route(REDIRECT_PATH)
def authorized():
    try:
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args
        )
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    except ValueError:
        pass
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    redirect_uri = url_for("index", _external=True)
    logout_url = f"{AUTHORITY}/oauth2/v2.0/logout?post_logout_redirect_uri={redirect_uri}"
    return redirect(logout_url)

@app.route("/public")
def public():
    return render_template("public.html")

@app.route("/profile")
def profile():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template("profile.html", user=session["user"])

@app.route("/groups")
def groups():
    if not session.get("user"):
        return redirect(url_for("login"))
    role = session["user"].get("roles", ["User"])[0]  # Default to "User" role
    print(role)
    # if not has_access(role, "groups"):
    #     return "Access Denied", 403
    # Placeholder for group membership logic
    groups = ["Group A", "Group B", "Group C"]  # Replace with actual Graph API call
    return render_template("groups.html", groups=groups)

@app.route("/graphcall")
def graphcall():
    # Add logic to handle the Graph API call or return a placeholder response
    return "Graph API call placeholder"

def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        CLIENT_ID, authority=authority or AUTHORITY, client_credential=CLIENT_SECRET, token_cache=cache
    )

def _build_auth_code_flow(authority=None, scopes=None):
    return _build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [], redirect_uri=url_for("authorized", _external=True)
    )

if __name__ == "__main__":
    app.run()
