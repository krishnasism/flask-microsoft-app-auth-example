variable "location" {
  description = "The Azure location where the resources will be created."
  type        = string
  default     = "West Europe"
}

variable "resource_group_name" {
  description = "The name of the resource group."
  type        = string
  default     = "flask-app-rg"
}

variable "ad_app_name" {
  description = "The name of the Azure AD application."
  type        = string
  default     = "flask-app"
}

variable "redirect_uris" {
  description = "The redirect URIs for the Azure AD application."
  type        = list(string)
  default = [
    "http://localhost:5000/getAToken",
    "http://127.0.0.1:5000/getAToken"
  ]
}

