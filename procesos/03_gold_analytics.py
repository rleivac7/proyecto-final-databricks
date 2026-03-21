# Databricks notebook source
# MAGIC %md
# MAGIC Gold Layer
# MAGIC
# MAGIC Este notebook contiene métricas agregadas generadas a partir de la capa Silver.
# MAGIC
# MAGIC Los datasets de esta capa están optimizados para análisis, generación de reportes y visualizaciones tipo dashboard, permitiendo obtener indicadores clave del negocio.
# MAGIC
# MAGIC La capa Gold representa la capa de consumo de negocio dentro de la arquitectura Medallion.

# COMMAND ----------

from pyspark.sql.functions import col,count,sum,avg

silver_df = spark.table("ralc_silver.sales_detail")

# COMMAND ----------

top_products = silver_df.groupBy("product_name") \
    .agg(count("*").alias("total_orders")) \
    .orderBy(col("total_orders").desc())

display(top_products)

top_products.write \
    .mode("overwrite") \
    .saveAsTable("ralc_gold.top_products")

# COMMAND ----------

reorders = silver_df.groupBy("product_name") \
    .agg(sum("reordered").alias("total_reorders")) \
    .orderBy(col("total_reorders").desc())

display(reorders)

reorders.write \
    .mode("overwrite") \
    .saveAsTable("ralc_gold.reorders")

# COMMAND ----------

orders_dow = silver_df.groupBy("order_dow") \
    .agg(count("*").alias("total_orders")) \
    .orderBy("order_dow")

display(orders_dow)

orders_dow.write \
    .mode("overwrite") \
    .saveAsTable("ralc_gold.orders_by_day")

# COMMAND ----------

top_departments = silver_df.groupBy("department_id") \
    .agg(count("*").alias("total_orders")) \
    .orderBy(col("total_orders").desc())

display(top_departments)

top_departments.write \
    .mode("overwrite") \
    .saveAsTable("ralc_gold.top_departments")

# COMMAND ----------

reorder_rate = silver_df.groupBy("product_name") \
    .agg(
        sum("reordered").alias("reorders"),
        count("*").alias("orders")
    ) \
    .withColumn("reorder_rate", col("reorders") / col("orders")) \
    .orderBy(col("reorder_rate").desc())

display(reorder_rate)

reorder_rate.write \
    .mode("overwrite") \
    .saveAsTable("ralc_gold.reorder_rate")

# COMMAND ----------

avg_products_per_order = silver_df.groupBy("order_id") \
    .count() \
    .agg(avg("count").alias("avg_products_per_order"))

display(avg_products_per_order)

avg_products_per_order.write \
    .mode("overwrite") \
    .saveAsTable("ralc_gold.avg_products_per_order")

# COMMAND ----------

print("Total registros en Silver:", silver_df.count())

print("Productos únicos:",
silver_df.select("product_id").distinct().count())

print("Órdenes únicas:",
silver_df.select("order_id").distinct().count())