## aws-serverless-data-lake
# Data Lake Serverless y Optimización de Costos en AWS

Diseño e implementación de una arquitectura de Data Lake Serverless utilizando Amazon S3, AWS Glue y Amazon Athena. El proyecto se centra en la ingesta de datos crudos de ventas, la automatización del descubrimiento de esquemas (schema discovery) y la optimización del rendimiento y costos de las consultas mediante la transformación de datos al formato Parquet (Columnar).

# Arquitectura:

* **Almacenamiento:** Amazon S3 (Arquitectura por capas: Raw vs Curated).
* **ETL/Descubrimiento:** AWS Glue Crawlers para la inferencia automática del esquema.
* **Analítica:** Amazon Athena (SQL Serverless).
* **Optimización:** Apache Parquet (Almacenamiento columnar) y Compresión Snappy.

| Métrica | CSV (Basado en Filas) | Parquet (Columnar) | Mejora |
| :--- | :--- | :--- | :--- |
| **Datos Escaneados** | 341 KB | 61 KB | **~82% de Reducción** |
| **Costo** | 100% (Referencia) | ~18% | **82% Más Barato** |
| **Rendimiento** | Escaneo Completo | Escaneo Selectivo | **Más Rápido** |

## Al convertir los datos históricos a formato Parquet, logré una reducción del 82% en los costos de escaneo de datos para consultas analíticas.

# Detalles de Implementación
* **1. Ingesta de Datos (Data Ingestion)**
   * Se generaron datos sintéticos de ventas utilizando un script de Python (src/generador_datos.py) y se almacenaron en un Bucket de S3 (zona /raw).

* **2. Descubrimiento de Esquema (Schema Discovery)**
   * Se configuró un AWS Glue Crawler para recorrer el bucket de S3, inferir los tipos de datos (String, Int, Float) y poblar automáticamente el AWS Glue Data Catalog.

* **3. Estrategia de Optimización (CTAS)**
   * Se utilizó Athena para transformar los datos CSV a formato Parquet utilizando una sentencia CTAS (Create Table As Select), moviendo los datos a la zona curated
 
   * CREATE TABLE "ventas_parquet"
WITH (
      format = 'PARQUET',
      external_location = 's3://.../curated/'
) AS
SELECT * FROM "raw_data";

# DINERO PERDIDO (Falta de optimización)
<img width="1389" height="673" alt="Captura de pantalla 2026-02-09 a la(s) 3 11 05 p m" src="https://github.com/user-attachments/assets/6d1a103e-e2ae-406c-8433-394eb2f1a416" />

# COSTO AHORRADO (Consulta optimizada)
<img width="1390" height="684" alt="Captura de pantalla 2026-02-09 a la(s) 3 12 36 p m" src="https://github.com/user-attachments/assets/062abb16-bab5-41f4-9b10-3118f5e58781" />

# Tech Stack (Tecnologías)
* Nube: AWS
* Lenguajes: SQL, Python
* Servicios: S3, Athena, Glue
