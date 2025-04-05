resource "azuread_application" "main" {
  display_name = var.ad_app_name
  owners       = [data.azuread_client_config.current.object_id]

  web {
    redirect_uris = var.redirect_uris
  }

  # Refer to: https://learn.microsoft.com/en-us/graph/permissions-reference
  required_resource_access {
    resource_app_id = "00000003-0000-0000-c000-000000000000" # Microsoft Graph
    resource_access {
      id   = "df021288-bdef-4463-88db-98f22de89214" # User.Read
      type = "Scope"
    }

    resource_access {
      id   = "b4e74841-8e56-480b-be8b-910348b18b4c" # User.ReadWrite
      type = "Scope"
    }
  }

  password {
    display_name = "${var.ad_app_name}-password"
  }
}

