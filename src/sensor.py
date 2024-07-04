import sys
import numpy as np
from datetime import date
import uuid


class Sensor:
    """
    Simulate a sensor at the entrance of a store
    take a mean a standard deviation of visitors
    """ ""

    def __init__(self, mean_visitor: int, std_dev_visitor: int) -> None:
        """
        initialize sensor
        """
        self.id = uuid.uuid4().int
        self.mean = mean_visitor
        self.std_dev = std_dev_visitor

    def get_number_visitors(self, hour: str, day: int, month: int, year: int) -> int:
        """ "
        Retrieve number of visitor for a specific date and hour
        and for a given sensor
        business_hour : hour selected by the user in format "%h:%m"
        return : number of visitor captured by the sensor for day business_day
        and hour business_hour
        """
        day = int(day)
        month = int(month)
        year = int(year)
        np.random.seed(seed=42)
        business_date = date(year, month, day)
        business_day_of_the_week = business_date.weekday()
        print(business_day_of_the_week)

        # multiplicator depending on a day
        proportion_visitors = [1, 1, 1.25, 1, 1.40, 1.5, 1]
        visitors = proportion_visitors[business_day_of_the_week] * np.random.normal(
            self.mean, self.std_dev
        )

        if (
            month == 8
            or business_day_of_the_week == 6
            or hour > "19:00"
            or hour < "09:00"
        ):
            number_visitors = 0
        else:
            if hour > "15:00" and hour < "19:00":
                number_visitors = 1.25 * visitors
            else:
                number_visitors = visitors

        return number_visitors


if __name__ == "__main__":
    if len(sys.argv) > 2:
        business_day, business_month, business_year = [
            d for d in sys.argv[1].split("-")
        ]
        business_hour = sys.argv[2]
        test_sensor = Sensor(1200, 1000)
        print(
            test_sensor.get_number_visitors(
                business_hour, business_day, business_month, business_year
            )
        )

    else:
        print("Please enter a date and a time")
