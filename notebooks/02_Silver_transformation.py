# Databricks notebook source
# MAGIC %md
# MAGIC Silver Layer
# MAGIC
# MAGIC Este notebook realiza la limpieza, transformación y unión de los datasets provenientes de la capa Bronze.
# MAGIC
# MAGIC En esta capa se aplican procesos de calidad de datos, normalización de tipos de datos y joins entre tablas para preparar la información para análisis posteriores.
# MAGIC
# MAGIC La capa Silver representa la capa de preparación de datos dentro de la arquitectura Medallion.

# COMMAND ----------

from pyspark.sql.functions import col

orders_df = spark.table("ralc_bronze.orders")
products_df = spark.table("ralc_bronze.products")
order_products_df = spark.table("ralc_bronze.order_products")

silver_df = order_products_df.alias("op") \
    .join(orders_df.alias("o"), col("op.order_id") == col("o.order_id"), "inner") \
    .join(products_df.alias("p"), col("op.product_id") == col("p.product_id"), "inner") \
    .select(
        col("op.order_id"),
        col("o.user_id"),
        col("o.eval_set"),
        col("o.order_number"),
        col("o.order_dow"),
        col("o.order_hour_of_day"),
        col("o.days_since_prior_order"),
        col("op.product_id"),
        col("op.add_to_cart_order"),
        col("op.reordered"),
        col("p.product_name"),
        col("p.aisle_id"),
        col("p.department_id")
    )

display(silver_df)

# COMMAND ----------

silver_df.write.mode("overwrite").saveAsTable("ralc_silver.sales_detail")

# COMMAND ----------

display(silver_df)

# COMMAND ----------

silver_df.write.mode("overwrite") \
.saveAsTable("ralc_silver.sales_detail")

# COMMAND ----------

print("Total registros:",silver_df.count())

print("Órdenes únicas:",
silver_df.select("order_id").distinct().count())

print("Productos únicos:",
silver_df.select("product_id").distinct().count())