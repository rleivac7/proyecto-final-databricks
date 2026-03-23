# Databricks notebook source
spark.sql("CREATE DATABASE IF NOT EXISTS ralc_bronze")
spark.sql("CREATE DATABASE IF NOT EXISTS ralc_silver")
spark.sql("CREATE DATABASE IF NOT EXISTS ralc_gold")

# COMMAND ----------

spark.sql("SHOW DATABASES").display()