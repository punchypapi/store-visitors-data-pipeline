import os

from pyspark.sql import SparkSession
from pyspark.sql import Window as W
from pyspark.sql import functions as F

# Initialize project path
project_path = os.environ["PYTHONPATH"]

# Create data folder in doesn't exist
if "processed" not in os.listdir(project_path + "/data"):
    os.mkdir(project_path + "/data/processed")

raw_sensor_data_path = project_path + "/data/raw/sensor_data.csv"
processed_sensor_data_path = project_path + "/data/processed"


spark = SparkSession.builder.appName("TransformData").getOrCreate()
# loading and reading data
sensor_data_df = spark.read.csv(raw_sensor_data_path, header=True)

# reformat data types
sensor_data_df = sensor_data_df.withColumn("date", F.to_date(F.col("date"), "d-M-yyyy"))
sensor_data_df = sensor_data_df.withColumn(
    "number_visitors", F.col("number_visitors").cast("int")
)
sensor_data_df = sensor_data_df.withColumn("sensor", F.col("sensor").cast("int"))

# get daily number visitors
sensor_data_df = (
    sensor_data_df.groupBy(["store", "sensor", "date"])
    .agg(F.sum("number_visitors").alias("daily_number_visitors"))
    .sort(["store", "sensor", "date"])
)
# add on a weekday column
sensor_data_df = sensor_data_df.withColumn("day_of_week", F.weekday("date") + 1).select(
    ["store", "sensor", "date", "day_of_week", "daily_number_visitors"]
)
# apply window function to get average of 4 latest week day partitioned by "store", "sensor", "day_of_week"
window = (
    W.partitionBy("store", "sensor", "day_of_week")
    .orderBy(F.asc("date"))
    .rowsBetween(-3, 0)
)
sensor_data_df = sensor_data_df.withColumn(
    "average_number_visitors_four_weekdays",
    F.avg("daily_number_visitors").over(window).cast("int"),
)

# add column pct_change to measure difference between number of visitors
sensor_data_df = sensor_data_df.withColumn(
    "pct_change (%)",
    F.when(F.col("daily_number_visitors") == 0, 0).otherwise(
        F.round(
            F.abs(
                F.col("daily_number_visitors")
                - F.col("average_number_visitors_four_weekdays")
            )
            / F.col("average_number_visitors_four_weekdays")
            * 100
        ).cast("int")
    ),
)
# export data in processed parquet format
try:
    sensor_data_df.write.parquet(processed_sensor_data_path, mode="overwrite")
    files = [
        file
        for file in os.listdir(processed_sensor_data_path)
        if file.endswith(".parquet")
    ]
    os.rename(
        processed_sensor_data_path + f"/{files[0]}",
        processed_sensor_data_path + f"/sensor_data.parquet",
    )

except Exception as e:
    print(f"An error has been encountered, logg : {e}")


# Stop the Spark session
spark.stop()
