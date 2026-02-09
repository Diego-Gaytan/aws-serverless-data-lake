-- Consulta 1: Escaneo costoso en CSV (Full Scan)
SELECT marca, SUM(precio) 
FROM "db_perfumeria_vip"."raw" 
GROUP BY marca;

-- Consulta 2: Escaneo barato en Parquet (Columnar Scan)
SELECT marca, SUM(precio) 
FROM "db_perfumeria_vip"."ventas_parquet" 
GROUP BY marca;
