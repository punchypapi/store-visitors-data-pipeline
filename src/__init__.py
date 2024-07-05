from src.sensor import Sensor


def create_sensor_data() -> dict:
    """
    create a dictionnary containing hourly sensor data between 2021
    and 2024
    """
    years_range = [i for i in range(2021, 2025)]
    months_range = [i for i in range(1, 13)]
    days_range = [i for i in range(1, 29)]
    hours_range = [f"0{i}:00" for i in range(10)] + [f"{i}:00" for i in range(10, 24)]

    sensor = Sensor(0.2, 1500, 400)
    sensor_data = {
        "id": [],
        "year": [],
        "month": [],
        "day": [],
        "hour": [],
        "visitors": [],
    }

    for business_year in years_range:
        for business_month in months_range:
            for business_day in days_range:
                for business_hour in hours_range:

                    number_visitors = sensor.get_number_visitor_error(
                        business_hour, business_day, business_month, business_year
                    )
                    sensor_data["id"].append(sensor.id)
                    sensor_data["year"].append(business_year)
                    sensor_data["month"].append(business_month)
                    sensor_data["day"].append(business_day)
                    sensor_data["hour"].append(business_hour)
                    sensor_data["visitors"].append(number_visitors)
    return sensor_data
