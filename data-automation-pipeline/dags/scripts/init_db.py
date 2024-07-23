import duckdb

# Initialize project path
project_path = "/opt/airflow"

parquet_path = project_path + "/data/processed/sensor_data.parquet"
duckdb_path = project_path + "/data/database/sensor_data.duckdb"

# Create a connection
con = duckdb.connect(duckdb_path, read_only=False)

# Create or replace the table in DuckDB
query = f"CREATE OR REPLACE TABLE sensor_data AS SELECT * FROM read_parquet('{parquet_path}')"

con.execute(query)
print("database initiated successfully")
con.close()
