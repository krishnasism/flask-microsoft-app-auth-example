resource "random_password" "main" {
  length  = 32
  special = false
}

resource "azurerm_key_vault_secret" "app_password" {
  depends_on   = [azurerm_role_assignment.main, azurerm_key_vault_access_policy.main]
  name         = "${var.ad_app_name}-password"
  value        = tolist(azuread_application.main.password).0.value
  key_vault_id = azurerm_key_vault.main.id
}
