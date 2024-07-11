import os

import duckdb
import pandas as pd
import plotly.express as px
import streamlit as st

# initialize project path
project_path = os.environ["PYTHONPATH"]

# Checking that data is loaded and transformed

if "sensor_data.csv" not in os.listdir(project_path + "/data/raw"):

    with open(project_path + "/get_number_visitors_api.py", "r") as f:
        exec(f.read())
    with open(project_path + "/src/data/script_generate_data.py", "r") as f:
        exec(f.read())
    with open(project_path + "/src/data/transform_data.py", "r") as f:
        exec(f.read())
    with open(project_path + "/src/data/init_db.py", "r") as f:
        exec(f.read())


if "sensor_data.parquet" not in os.listdir(project_path + "/data/processed"):

    with open(project_path + "/src/data/transform_data.py", "r") as f:
        exec(f.read())
    with open(project_path + "/src/data/init_db.py", "r") as f:
        exec(f.read())

if "sensor_data.duckdb" not in os.listdir(project_path + "/data/database"):

    with open(project_path + "/src/data/init_db.py", "r") as f:
        exec(f.read())

# Connecting to database
con = duckdb.connect(
    project_path + "/data/database/sensor_data.duckdb", read_only=False
)

# Retrieve table and convert it to DataFrame
sensor_data_df = con.execute("SELECT * FROM sensor_data").df()

# Reformatting date column
sensor_data_df["date"] = pd.to_datetime(sensor_data_df["date"]).dt.date

st.write("Tracking visitors stores")

with st.sidebar:

    store_selection = st.selectbox(
        "Store :", list(sensor_data_df.store.unique()), placeholder="select the store"
    )
    sensor_selection = st.selectbox(
        "Sensor :",
        list(sensor_data_df.sensor.unique()),
        placeholder="select the sensor",
    )

    # filter DataFrame on user selection
    store_sensor_df = sensor_data_df[
        (sensor_data_df.store == store_selection)
        & (sensor_data_df.sensor == sensor_selection)
    ]


# plot bar to display distribution of visitors across dates
distribution_visitors = px.bar(store_sensor_df, x="date", y="daily_number_visitors")
st.write(
    f"Yearly visitors distribution for store {store_selection} and sensor {sensor_selection} :",
    distribution_visitors,
)
# retrieve threshold to filter pct_change column
pct_change_threshold = st.number_input(
    "Select percentage change threshold",
    min_value=10,
    max_value=60,
    value=30,
    step=10,
    format="%d",
)
store_sensor_outliers_df = store_sensor_df[
    store_sensor_df["pct_change (%)"] > pct_change_threshold
]

# plot a scatter plot to display outliers
outliers_scatter = px.scatter(store_sensor_outliers_df, x="date", y="pct_change (%)")
st.write(
    f"Outliers detected in visitors for store {store_selection} and sensor {sensor_selection} for threshold set to {pct_change_threshold} :",
    outliers_scatter,
)

# display dataframe according to user filter
st.write(
    f"Daily visitors for store {store_selection} captured by sensor {sensor_selection} :",
    store_sensor_df,
)
