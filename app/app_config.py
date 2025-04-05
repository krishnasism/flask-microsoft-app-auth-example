import os

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTHORITY = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}"
REDIRECT_PATH = os.getenv("REDIRECT_PATH", "/getAToken") 
SCOPE = os.getenv("SCOPE", "").split(",")
