# Diccionario de datos

## orders.csv
- order_id: identificador único de la orden
- user_id: identificador del usuario
- eval_set: partición del dataset
- order_number: número secuencial de la orden para el usuario
- order_dow: día de la semana de la orden
- order_hour_of_day: hora del día de la orden
- days_since_prior_order: días transcurridos desde la orden previa

## products.csv
- product_id: identificador único del producto
- product_name: nombre del producto
- aisle_id: identificador del pasillo/categoría
- department_id: identificador del departamento

## order_products__train.csv
- order_id: identificador de la orden
- product_id: identificador del producto
- add_to_cart_order: posición en la que se agregó al carrito
- reordered: indicador de recompra del producto
