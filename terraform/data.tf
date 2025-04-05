data "azuread_client_config" "current" {}

data "azurerm_client_config" "current" {}

data "http" "host_ip" {
    url = "https://ipv4.icanhazip.com"
}
