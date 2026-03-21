# Databricks notebook source
# MAGIC %md
# MAGIC Bronze Layer
# MAGIC
# MAGIC Este notebook realiza la ingesta de los datasets originales (archivos CSV) desde el Data Lake hacia tablas Delta en Databricks.
# MAGIC
# MAGIC En esta capa los datos se almacenan en su forma más cercana a la fuente original, agregando metadata como el archivo de origen y la fecha de ingestión para permitir trazabilidad y control del proceso ETL.
# MAGIC
# MAGIC La capa Bronze representa la capa de datos crudos dentro de la arquitectura Medallion.

# COMMAND ----------

orders_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/ralc_bronze/raw_files/orders.csv")

display(orders_df)

# COMMAND ----------

products_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/ralc_bronze/raw_files/products.csv")

display(products_df)

# COMMAND ----------

order_products_df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/Volumes/workspace/ralc_bronze/raw_files/order_products__train.csv")

display(order_products_df)

# COMMAND ----------

orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ";") \
    .load("/Volumes/workspace/ralc_bronze/raw_files/orders.csv")

display(orders_df)

# COMMAND ----------

orders_df.write.mode("overwrite").saveAsTable("ralc_bronze.orders")

# COMMAND ----------

products_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ";") \
    .load("/Volumes/workspace/ralc_bronze/raw_files/products.csv")

display(products_df)

# COMMAND ----------

order_products_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ";") \
    .load("/Volumes/workspace/ralc_bronze/raw_files/order_products__train.csv")

display(order_products_df)

# COMMAND ----------

products_df.write.mode("overwrite").saveAsTable("ralc_bronze.products")
order_products_df.write.mode("overwrite").saveAsTable("ralc_bronze.order_products")