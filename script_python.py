import datetime
import sys

import requests

# //!\\ Warning : please make sure to run get_number_visitors_api.py to start the server before running this script


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


# retrieving inputs using a dialog box

# while True:
#     inputted_store = input("Select store between Lille, Paris, Toulouse : ")
#     inputted_sensor_id = input("Select a sensor id  between 1 and 8 : ")
#     inputted_business_date = input("Select date in format dd-mm-yyyy : ")
#     inputted_business_hour = input(
#         "Select an hour in format hh:mm (if no hour is selected we default it to 12:00) : "
#     )
#
#     print(
#         f"Number of visitors for store {inputted_store} captured bu the sensor number {inputted_sensor_id} during {inputted_business_date} at {inputted_business_hour} :{retrieve_visitor_api(inputted_store, inputted_sensor_id,inputted_business_date,inputted_business_hour)}"
#     )


# retrieving inputs using terminal arguments
if len(sys.argv) > 3:
    inputted_store = str(sys.argv[1])
    inputted_sensor_id = int(sys.argv[2])
    inputted_business_date = sys.argv[3]
    if len(sys.argv) > 4:
        inputted_business_hour = sys.argv[4]
    else:
        inputted_business_hour = ""

    try:
        int(
            retrieve_visitor_api(
                inputted_store,
                inputted_sensor_id,
                inputted_business_date,
                inputted_business_hour,
            )
        )
        if len(sys.argv) > 4:
            print(
                f"Number of visitors for store {inputted_store} captured bu the sensor number {inputted_sensor_id} during {inputted_business_date} at {inputted_business_hour} : {retrieve_visitor_api(inputted_store, inputted_sensor_id, inputted_business_date, inputted_business_hour)}"
            )
        else:
            print(
                f"Number of visitors for store {inputted_store} captured bu the sensor number {inputted_sensor_id} during {inputted_business_date} at 12:00 : {retrieve_visitor_api(inputted_store, inputted_sensor_id, inputted_business_date, inputted_business_hour)}"
            )

    except Exception as e:
        print(
            retrieve_visitor_api(
                inputted_store,
                inputted_sensor_id,
                inputted_business_date,
                inputted_business_hour,
            ).strip('"')
        )

else:
    print("Not enough inputs, please retry")
