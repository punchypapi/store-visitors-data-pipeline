import csv
from datetime import datetime

from tests.test_sensor_api import retrieve_visitor_api

# //!\\ Warning : please make sure to run get_number_visitors_api.py to start the server before running this script

sensor_data = [["store", "sensor", "date", "hour", "number_visitors"]]

store_locations = ["Lille", "Paris", "Toulouse"]
business_year = 2024
months_range = [i for i in range(1, 13)]
days_range = [i for i in range(1, 29)]
hours_range = [f"0{i}:00" for i in range(10)] + [f"{i}:00" for i in range(10, 24)]

for store_sensor in store_locations:
    for id_sensor in range(1, 4):
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
sensor_data_csv = "data/raw/sensor_data.csv"

# Write data to CSV file
with open(sensor_data_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sensor_data)

print(f"Data has been written successfully to {sensor_data_csv}")
