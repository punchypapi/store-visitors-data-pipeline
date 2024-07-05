import datetime
import sys

if len(sys.argv) > 1:
    inputed_date = sys.argv[1]
    try:
        print(datetime.datetime.strptime(inputed_date, "%d-%m-%Y").date())
    except ValueError:
        print("please enter a valid date with format '%d-%m-%Y'")
