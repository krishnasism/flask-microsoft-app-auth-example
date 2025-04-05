resource "azurerm_key_vault" "main" {
  name                = "${var.ad_app_name}-kv"
  location            = var.location
  resource_group_name = azurerm_resource_group.main.name
  sku_name            = "standard"
  tenant_id           = data.azuread_client_config.current.tenant_id

  network_acls {
    default_action = "Deny"
    bypass         = "AzureServices"

    ip_rules = [trimspace(chomp(data.http.host_ip.response_body))]
  }
}
