terraform {
  required_providers {
    azuread = {
      source  = "hashicorp/azuread"
      version = "3.3.0"
    }

    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.26.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.7.1"
    }

    http = {
      source = "hashicorp/http"
      version = "3.4.5"
    }
  }
}

provider "azuread" {
}

provider "random" {

}

provider "azurerm" {
  features {}
}

provider "http" {
}
