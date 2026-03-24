## Resumen del proyecto

Pipeline ETL end-to-end  
Arquitectura Medallion  
Gobierno básico de datos  
Modelo de seguridad  
Visualizaciones analíticas  
Estructura profesional de proyecto

# Proyecto ETL en Databricks – Arquitectura Medallion

## Descripción del proyecto

Este proyecto implementa un pipeline ETL completo utilizando Databricks Free Edition siguiendo la arquitectura Medallion (Bronze, Silver y Gold).

El objetivo es demostrar un flujo completo de ingeniería de datos que incluye:

- Ingesta de datos
- Transformación de datos
- Modelado de datos
- Gobierno básico de datos
- Implementación de seguridad
- Generación de métricas analíticas
- Documentación del proyecto

---

## Arquitectura del proyecto

El proyecto sigue el patrón de arquitectura Medallion:

Bronze Layer → Datos crudos  
Silver Layer → Datos transformados  
Gold Layer → Datos listos para análisis  

Flujo del pipeline:

Archivos CSV → Tablas Bronze → Transformaciones Silver → Tablas Gold → Visualizaciones

---

## Tecnologías utilizadas

- Databricks Free Edition
- Apache Spark (PySpark)
- Delta Lake
- Unity Catalog
- SQL
- Python
- GitHub

---

## Descripción del dataset

El proyecto utiliza un dataset de comercio electrónico que contiene información de:

Órdenes  
Productos  
Relación entre órdenes y productos  

Principales entidades:

Orders:
Información sobre el comportamiento de compra de los usuarios.

Products:
Catálogo de productos disponibles.

Order Products:
Relación entre órdenes y productos comprados.

---

## Proceso ETL

### Bronze Layer

En esta capa se cargan los archivos CSV originales hacia tablas Delta.

Objetivos:

Preservar la estructura original  
Agregar metadata de ingestión  
Permitir trazabilidad del proceso  

---

### Silver Layer

En esta capa se realizan transformaciones:

Joins entre tablas  
Limpieza de datos  
Normalización de tipos  
Modelado de datos  

Se genera una tabla consolidada para análisis.

---

### Gold Layer

En esta capa se generan datasets listos para análisis de negocio:

Productos más vendidos  
Órdenes por día  
Productos con mayor tasa de recompra  
Promedio de productos por orden  

Esta capa está optimizada para consumo analítico y generación de reportes.

---

## Modelo de seguridad

Se implementó un modelo básico de gobierno de datos utilizando Unity Catalog:

Data Engineers:
Acceso a Bronze y Silver.

Data Analysts:
Acceso a Silver y Gold.

Business Users:
Acceso únicamente a Gold.

La seguridad fue implementada mediante GRANT sobre las tablas generadas.

---

## Estructura del proyecto

datasets/ → Insumos del ETL
dashboard/ → Visualizaciones analíticas
reversion/ → Scripts de reversión
seguridad/ → Modelo de seguridad
PrepAmb/ → Preparación del ambiente
proceso/ → Notebooks ETL
evidencias/ → Evidencias de ejecución
certificaciones/ → Evidencia de formación
README.md → Documentación principal


---

## Resultados obtenidos

El proyecto demuestra:

Implementación completa de ETL  
Uso de arquitectura Medallion  
Gobierno básico de datos  
Implementación de seguridad  
Preparación de datos para analytics  
Estructura de proyecto profesional  

---

## Dashboard

Las visualizaciones generadas muestran:

Productos más vendidos  
Patrones de compra por día  
Comportamiento de recompra  

Todas las métricas provienen de la capa Gold.

---

## Reproducibilidad

El proyecto incluye:

Scripts de preparación de ambiente  
Notebooks ETL  
Scripts de seguridad  
Scripts de reversión  

Esto permite reconstruir el entorno del proyecto.

---

## Autor

Roberto Leiva  

Profesional en informática médica en transición hacia el área de Ingeniería de Datos.

Experiencia en:

Sistemas médicos (PACS / RIS)
Integración de datos
Virtualización
SQL
Plataformas de datos

---

## Conclusión

Este proyecto demuestra conocimientos prácticos de ingeniería de datos moderna utilizando Databricks y principios de arquitectura Medallion, aplicando buenas prácticas de organización, seguridad y análisis de datos.
