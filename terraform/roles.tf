resource "azurerm_role_assignment" "main" {
  principal_id         = data.azuread_client_config.current.object_id
  role_definition_name = "Key Vault Contributor"
  scope                = azurerm_key_vault.main.id
}

resource "azurerm_key_vault_access_policy" "main" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = [
    "Get", "List", "Set", "Delete", "Recover", "Backup", "Restore", "Purge"
  ]
}
