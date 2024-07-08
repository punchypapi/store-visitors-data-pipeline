import sys
from tests import retrieve_visitor_api

# //!\\ Warning : please make sure to run get_number_visitors_api.py to start the server before running this script


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
    print("Not enough inputs, please try again")
