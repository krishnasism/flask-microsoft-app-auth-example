output "app_password" {
  sensitive = true
  value     = tolist(azuread_application.main.password).0.value
}

output "client_id" {
  value = azuread_application.main.client_id
}
