import datetime

import requests


def retrieve_visitor_api(
    business_store, sensor_id, business_date: str, business_hour: str
) -> int | str:
    """
    Retrieve from the GET API number of visitor captured by the sensor
    for a given datetime
    """
    # check the validity of the date
    try:
        datetime.datetime.strptime(business_date, "%d-%m-%Y").date()

        day = int(f"{business_date.split("-")[0]}")
        month = int(f"{business_date.split("-")[1]}")
        year = int(f"{business_date.split("-")[2]}")

        if business_hour == "":
            business_hour = "12:00"

        url = f"http://0.0.0.0:8080/?selected_store={business_store}&selected_id={sensor_id}&selected_day={day}&selected_month={month}&selected_year={year}&selected_hour={business_hour}"
        response = requests.get(url).text
        return response

    except Exception as e:
        return 'please enter a valid date with format "dd-mm-yyyy"'
