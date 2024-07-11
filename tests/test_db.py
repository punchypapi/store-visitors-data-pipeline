import os

import duckdb

project_path = os.environ["PYTHONPATH"]
duckdb_path = project_path + "/data/database/sensor_data.duckdb"
con = duckdb.connect(duckdb_path, read_only=False)
print(con.execute("SELECT * FROM sensor_data").df())
