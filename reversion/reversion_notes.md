# Reversión del proyecto

## Objetivo
Esta carpeta contiene scripts para revertir los objetos creados durante el desarrollo del pipeline ETL en Databricks.

## Alcance
Se contemplan dos tipos de reversión:

### Reversión lógica
Eliminación de tablas creadas en las capas Bronze, Silver y Gold.

### Reversión física
Eliminación del volumen utilizado como capa raw para almacenar los archivos fuente.

## Nota
La reversión debe ejecutarse con precaución, ya que elimina permanentemente los objetos creados para el proyecto.
