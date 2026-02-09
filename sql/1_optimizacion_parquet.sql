-- Convertir datos CSV (Raw) a Parquet (Optimized)
-- Reemplaza con tu bucket real si es necesario
CREATE TABLE "db_perfumeria_vip"."ventas_parquet"
WITH (
      format = 'PARQUET',
      external_location = 's3://datalake-perfumeria-diego-2026/curated/ventas_parquet/'
) AS
SELECT * FROM "db_perfumeria_vip"."raw";

