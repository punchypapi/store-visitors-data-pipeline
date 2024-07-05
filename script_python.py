import datetime
import subprocess
import sys

import requests


def start_api_server():
    """
    Start the API server
    """
    global process
    print("Starting local API server...")
    process = subprocess.Popen(["python", "get_number_visitors_api.py"])
    print("Server started. Process ID:", process.pid)


def stop_api_server():
    """
    Shutdown the API server
    """
    global process
    if process:
        print("Terminating server process...")
        process.terminate()
        process.wait()  # Wait for the process to terminate completely
        print("Server process terminated.")


# starting the API server in the background
start_api_server()


def retrieve_visitor_api(business_date: str) -> int:
    """
    Retrieve from the GET API number of visitor captured by the sensor
    for a given datetime
    """
    # check the validity of the date
    try:
        datetime.datetime.strptime(business_date, "%d-%m-%Y").date()
    except ValueError:
        print("please enter a valid date with format 'dd-mm-yyyy'")

    day = int(business_date.split("-")[0])
    month = int(business_date.split("-")[1])
    year = int(business_date.split("-")[2])

    url = f"http://0.0.0.0:8000/?day={day}&month={month}&year={year}"
    response = int(requests.get(url).text)
    return response


if len(sys.argv) > 1:
    inputed_business_date = sys.argv[1]
    print(
        f"Number of visitors for {inputed_business_date} :{retrieve_visitor_api(inputed_business_date)}"
    )

stop_api_server()
