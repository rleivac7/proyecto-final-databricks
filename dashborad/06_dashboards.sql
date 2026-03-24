-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Gold Layer Analytics Dashboard
-- MAGIC
-- MAGIC This notebook demonstrates business insights generated from the Gold layer of the Medallion Architecture.
-- MAGIC
-- MAGIC The objective is to show that the ETL pipeline produces datasets ready for reporting and business analytics.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Top Selling Products
-- MAGIC
-- MAGIC This visualization shows the most frequently ordered products in the dataset.
-- MAGIC This helps identify high demand products and consumption patterns.

-- COMMAND ----------

print("Total registros en Silver:", silver_df.count())

print("Productos únicos:",
silver_df.select("product_id").distinct().count())

print("Órdenes únicas:",
silver_df.select("order_id").distinct().count())

-- COMMAND ----------

top_products = spark.table("ralc_gold.top_products")
display(top_products.limit(10))

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Orders Distribution by Day of Week
-- MAGIC
-- MAGIC This visualization shows customer ordering behavior patterns by day.
-- MAGIC Useful for demand planning and operational insights.

-- COMMAND ----------

orders_by_day = spark.table("ralc_gold.orders_by_day")
display(orders_by_day)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Product Reorder Behavior
-- MAGIC
-- MAGIC This analysis shows which products have the highest reorder rate, indicating customer loyalty or product dependency.

-- COMMAND ----------

reorder_rate = spark.table("ralc_gold.reorder_rate")

display(reorder_rate.orderBy("reorder_rate", ascending=False).limit(10))

-- COMMAND ----------

avg_products = spark.table("ralc_gold.avg_products_per_order")

display(avg_products)