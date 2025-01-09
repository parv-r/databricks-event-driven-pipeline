# Databricks notebook source
# DBTITLE 1,Initialize the source, and target directory  and the stage table
source_dir = "/Volumes/incremental_load/default/orders_data/source/"
target_dir = "/Volumes/incremental_load/default/orders_data/archive/"
stage_table = "incremental_load.default.orders_stage"

# COMMAND ----------

# DBTITLE 1,Read files from source directory
# Read CSV file from dbfs path under staging_zn folder
df = spark.read.csv(source_dir, header=True, inferSchema=True)

# COMMAND ----------

# DBTITLE 1,Overwrite the data into stage table
# Create Delta table named stage_zn if it doesn't exist and overwrite the data in stage table
df.write.format("delta").mode("overwrite").saveAsTable(stage_table)

# COMMAND ----------

# List all files in the source directory
files = dbutils.fs.ls(source_dir)

# Iterate on the list one by one and print each file path separately
for file in files:
    src_path = file.path

    # Construct the target path
    target_path = target_dir + src_path.split("/")[-1]
    
    # Move the file
    dbutils.fs.mv(src_path, target_path)
