-- Databricks notebook source


-- COMMAND ----------

GRANT USE SCHEMA ON SCHEMA ralc_gold TO `data_analysts`;
GRANT USE SCHEMA ON SCHEMA ralc_gold TO `business_users`;

GRANT SELECT ON TABLE ralc_gold.top_products TO `data_analysts`;
GRANT SELECT ON TABLE ralc_gold.top_products TO `business_users`;

GRANT SELECT ON TABLE ralc_gold.reorders TO `data_analysts`;
GRANT SELECT ON TABLE ralc_gold.reorders TO `business_users`;

GRANT SELECT ON TABLE ralc_gold.orders_by_day TO `data_analysts`;
GRANT SELECT ON TABLE ralc_gold.orders_by_day TO `business_users`;

-- COMMAND ----------

GRANT USE SCHEMA ON SCHEMA ralc_silver TO `data_engineers`;
GRANT USE SCHEMA ON SCHEMA ralc_silver TO `data_analysts`;

GRANT SELECT ON TABLE ralc_silver.sales_detail TO `data_engineers`;
GRANT SELECT ON TABLE ralc_silver.sales_detail TO `data_analysts`;

-- COMMAND ----------

GRANT USE SCHEMA ON SCHEMA ralc_bronze TO `data_engineers`;

GRANT SELECT ON TABLE ralc_bronze.orders TO `data_engineers`;
GRANT SELECT ON TABLE ralc_bronze.products TO `data_engineers`;
GRANT SELECT ON TABLE ralc_bronze.order_products TO `data_engineers`;

-- COMMAND ----------

SHOW GRANTS ON TABLE ralc_gold.top_products;

-- COMMAND ----------

SHOW GRANTS ON TABLE ralc_silver.sales_detail;