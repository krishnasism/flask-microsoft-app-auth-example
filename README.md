# flask-microsoft-ad
Flask App Template w/ Microsoft AD authentication

## Prerequisites
1. [Terraform](https://developer.hashicorp.com/terraform/downloads).
2. [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
3. [Python](https://www.python.org/)

## Setting Up the Environment

### 1. Create a Service Principal
```sh
az ad sp create-for-rbac --name terraform-sp --role Owner --scopes /subscriptions/<Subscription ID>
```

### 2. Configure Environment Variables
Create a `.env` file in the `app` and `terraform` directories based on the provided `.env.example` files.

#### Example for `app/.env`:
```env
CLIENT_ID="your-client-id"
CLIENT_SECRET="your-client-secret"
AUTHORITY="https://login.microsoftonline.com/your-tenant-id"
```

#### Example for `terraform/.env`:
```env
ARM_CLIENT_ID="your-client-id"
ARM_CLIENT_SECRET="your-client-secret"
ARM_SUBSCRIPTION_ID="your-subscription-id"
ARM_TENANT_ID="your-tenant-id"
```

### 3. Initialize Terraform
Navigate to the `terraform` directory and run:
```sh
terraform init
terraform apply
```
This will create the necessary Azure resources, including the Key Vault and app registration.

### 4. Retrieve Secrets
After applying Terraform, retrieve the `app_password` and `client_id` from the Terraform outputs or Azure Key Vault. Update the `.env` files accordingly.

## Running the Flask App

### 1. Install Dependencies
Navigate to the `app` directory and install dependencies:
```sh
pip install -r requirements.txt
```

### 2. Run the App
Start the Flask app:
```sh
python app.py
```

The app will be available at `http://localhost:5000`.

## Additional Notes

### Assign Permissions
Ensure the app has the necessary Microsoft Graph API permissions:
```sh
az ad app permission add \
  --id <SP ID> \
  --api 00000003-0000-0000-c000-000000000000 \
  --api-permissions 19dbc75e-c2e2-444c-a770-ec69d8559fc7=Role

az ad app permission add \
  --id <SP ID> \
  --api 00000003-0000-0000-c000-000000000000 \
  --api-permissions 62a82d76-70ea-41e2-9197-370581804d09=Role

az ad app permission add \
  --id <SP ID> \
  --api 00000003-0000-0000-c000-000000000000 \
  --api-permissions 9e3f62cf-ca93-4989-b6ce-bf83c28f9fe8=Role

az ad app permission admin-consent --id <SP ID>
```

### Debugging
If you encounter issues, verify:
1. Environment variables are correctly set.
2. Azure resources are properly provisioned.
3. Permissions are granted and admin consent is provided.