import csv
from datetime import datetime

import requests

"""
This script generate hourly sensor data from 3 sensors for three different store
starting from 01-01-2024 until the day the script is run 
"""

# Initialize project path
project_path = "/opt/airflow"


def retrieve_visitor_api(
    business_store, sensor_id, business_date: str, business_hour: str
) -> int | str:
    """
    Retrieve from the GET API number of visitor captured by the sensor
    for a given datetime
    """

    day = int(f"{business_date.split("-")[0]}")
    month = int(f"{business_date.split("-")[1]}")
    year = int(f"{business_date.split("-")[2]}")

    if business_hour == "":
        business_hour = "12:00"

    url = f"http://fastapi-server:8000/?selected_store={business_store}&selected_id={sensor_id}&selected_day={day}&selected_month={month}&selected_year={year}&selected_hour={business_hour}"

    response = requests.get(url)
    return response.text


sensor_data = [["store", "sensor", "date", "hour", "number_visitors"]]

store_locations = ["Lille", "Paris"]
business_year = 2024
months_range = [i for i in range(1, 13)]
days_range = [i for i in range(1, 29)]
hours_range = [f"0{i}:00" for i in range(10)] + [f"{i}:00" for i in range(10, 24)]


for store_sensor in store_locations:
    for id_sensor in range(1, 3):
        for business_month in months_range:
            for business_day in days_range:
                for business_hour in hours_range:

                    business_date = f"{business_day}-{business_month}-{business_year}"
                    # comparing date selected with today
                    if (
                        datetime.strptime(business_date, "%d-%m-%Y").date()
                        <= datetime.now().date()
                    ):
                        number_visitors = retrieve_visitor_api(
                            store_sensor, id_sensor, business_date, business_hour
                        )
                        sensor_data.append(
                            [
                                store_sensor,
                                id_sensor,
                                business_date,
                                business_hour,
                                number_visitors,
                            ]
                        )


# Specify the file path
sensor_data_csv = project_path + "/data/raw/sensor_data.csv"

# Write data to CSV file
with open(sensor_data_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sensor_data)

print(f"Data has been written successfully to {sensor_data_csv}")
