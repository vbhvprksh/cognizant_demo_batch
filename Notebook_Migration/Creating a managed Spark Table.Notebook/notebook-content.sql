-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   }
-- META }

-- MARKDOWN ********************

-- # Creating a managed Spark table
-- This notebook describes how to create a managed table from Spark. 
-- The table is created in the Synapse warehouse folder in your primary storage account. The table will be synchronized and available in Synapse SQL Pools. 


-- CELL ********************

DROP TABLE IF EXISTS cities

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

CREATE TABLE cities
  (name STRING, population INT)
  USING PARQUET

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- MARKDOWN ********************

-- Insert a few rows into the table using a list of values.


-- CELL ********************

INSERT INTO cities VALUES ('Seattle', 730400), ('San Francisco', 881549), ('Beijing', 21540000), ('Bangalore', 10540000)

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- MARKDOWN ********************

-- * Retrieve values back. Click on 'Chart' below to review the visualization.


-- CELL ********************

SELECT * FROM cities ORDER BY name

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- MARKDOWN ********************

-- Drop the table. Please note the data will get deleted from the primary storage account associated with this workspace.


-- CELL ********************

DROP TABLE cities

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
