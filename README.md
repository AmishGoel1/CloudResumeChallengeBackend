# 🌐 Azure Backend Project - API and Cosmos DB Table Integration

This project sets up a backend API using Azure Functions and connects it to an Azure Cosmos DB Table API, all deployed in Azure's serverless environment. Here's a step-by-step breakdown of the setup and configuration.

---

## 🏗️ Resource Group Setup

- **Created a new resource group** through the Azure portal (GUI).
- Chose default settings suitable for backend APIs and low-memory usage.

---
cd 
## ⚡ Azure Function App Deployment

- **Created a Function App** through the Azure portal (GUI).
- Selected:
  - **Flex consumption tier** (scalable and cost-effective).
  - **Python runtime** (version 3.12).
  - **Lowest memory** tier since backend API is lightweight.
  - Other default settings for simplicity.
- Deployed the Function App successfully.

---

## 🗃️ Azure Cosmos DB Table Setup

- **Created an Azure Cosmos DB Table** through the Azure portal.
- Used the Table API to store and retrieve data for the backend API.

---

## 🐍 Working with Python Azure Functions

- **Followed the Microsoft Docs guide**: [Create your first function using Python](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python)
- **Installed Azure Functions Core Tools** for local development:
  - To uninstall: `brew uninstall azure-functions-core-tools@4`
- **Set up a virtual Python environment**:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
