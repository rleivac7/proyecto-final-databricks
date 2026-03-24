-- GOLD LAYER
DROP TABLE IF EXISTS ralc_gold.top_products;
DROP TABLE IF EXISTS ralc_gold.reorders;
DROP TABLE IF EXISTS ralc_gold.orders_by_day;
DROP TABLE IF EXISTS ralc_gold.top_departments;
DROP TABLE IF EXISTS ralc_gold.reorder_rate;
DROP TABLE IF EXISTS ralc_gold.avg_products_per_order;

-- SILVER LAYER
DROP TABLE IF EXISTS ralc_silver.sales_detail;

-- BRONZE LAYER
DROP TABLE IF EXISTS ralc_bronze.orders;
DROP TABLE IF EXISTS ralc_bronze.products;
DROP TABLE IF EXISTS ralc_bronze.order_products;
