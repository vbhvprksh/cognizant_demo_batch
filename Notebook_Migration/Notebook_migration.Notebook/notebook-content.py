# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "02dd11b9-d551-4ed1-9ec0-b7465abe440f",
# META       "default_lakehouse_name": "Notebook_lkh",
# META       "default_lakehouse_workspace_id": "29dc2f4d-d987-48f6-aa6f-0064f1f662a6",
# META       "known_lakehouses": [
# META         {
# META           "id": "02dd11b9-d551-4ed1-9ec0-b7465abe440f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************


azure_client_id = "17302058-9106-498c-8073-927ed9bcbffe"
azure_tenant_id = "cc5fbd94-dbc7-488d-8dd6-e68e03608a50"
azure_client_secret = "516f4d04-e1af-4971-b900-828acd6663fa"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Azure Synapse workspace config
synapse_workspace_name = "cognizantbatch"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Fabric config
workspace_id = "29dc2f4d-d987-48f6-aa6f-0064f1f662a6"
lakehouse_id = "02dd11b9-d551-4ed1-9ec0-b7465abe440f"
export_folder_name = f"export/{synapse_workspace_name}"
prefix = "" # this prefix is used during import {prefix}{notebook_name}
output_folder = f"abfss://00000Demos@onelake.dfs.fabric.microsoft.com/Notebook_lkh.Lakehouse/Files{export_folder_name}"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Scenario: Listing files from Lakehouse / mounted storage

# CELL ********************

# List files in DBFS or mounted path
dbutils.fs.ls("dbfs:/mnt/data")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Correct way in Fabric
notebookutils.fs.ls("Files/")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Scenario: Reading secrets

# CELL ********************

dbutils.secrets.get(scope="my_scope", key="storage_key")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Currently, Fabric does not have secrets under notebookutils.
# Instead, you use Key Vault integration or Linked services → credentials are handled outside the notebook.
# Trying notebookutils.secrets.get() → ❌ Error.

# MARKDOWN ********************

# ### Scenario: Displaying widgets

# CELL ********************

dbutils.widgets.text("param1", "default")
param_value = dbutils.widgets.get("param1")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
