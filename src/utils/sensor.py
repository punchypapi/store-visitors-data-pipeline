from datetime import date

import numpy as np


class Sensor:
    """
    Simulate a sensor at the entrance of a store
    take a mean a standard deviation of visitors
    """ ""

    def __init__(
        self,
        proba_error_sensor: float,
        sensor_mean_visitor: int,
        sensor_std_dev_visitor: int,
    ) -> None:
        """
        initialize sensor
        """
        self.mean = sensor_mean_visitor
        self.std_dev = sensor_std_dev_visitor
        self.proba_error = proba_error_sensor

    def get_number_visitors(self, hour: str, day: int, month: int, year: int) -> int:
        """ "
        Retrieve number of visitor for a specific day and hour
        and for a given sensor
        business_hour : hour selected by the user in format "%h:%m"
        return : number of visitor captured by the sensor for a specific day
        and hour business_hour
        """
        day = int(day)
        month = int(month)
        year = int(year)
        # np.random.seed(seed=42)
        business_date = date(year, month, day)
        business_day_of_the_week = business_date.weekday()

        # multiplicator depending on a day
        proportion_visitors = [1, 1, 1.25, 1, 1.40, 1.5, 1]
        visitors = proportion_visitors[business_day_of_the_week] * abs(
            np.random.normal(self.mean, self.std_dev)
        )

        if (
            month == 8
            or business_day_of_the_week == 6
            or hour > "19:00"
            or hour < "09:00"
        ):
            number_visitors = 0
        else:
            if hour >= "15:00" and hour < "19:00":
                number_visitors = 1.25 * visitors
            else:
                number_visitors = visitors

        return int(number_visitors)

    def get_number_visitor_error(
        self, hour: str, day: int, month: int, year: int
    ) -> int:
        """ "
        Retrieve number of visitor for a specific date and hour
        and for a given sensor while taking into account errors
        business_hour : hour selected by the user in format "%h:%m"
        return : number of visitor captured by the sensor for day business_day
        and hour business_hour
        """

        visitors = self.get_number_visitors(hour, day, month, year)
        if visitors > 0:
            odd_error = int(self.proba_error * 100)
            list_odd = [int(visitors / 6) for i in range(odd_error)] + [
                visitors for i in range(100 - odd_error)
            ]
            visitors = np.random.choice(list_odd)
        return visitors


if __name__ == "__main__":

    hours_range = [f"0{i}:00" for i in range(10)] + [f"{i}:00" for i in range(10, 24)]
    business_year = 2021
    business_month = 3
    for business_day in range(1, 29):
        for business_hour in hours_range:
            test_sensor = Sensor(0.2, 3000, 100)
            print(
                f"{business_day}-{business_month}-{business_year}",
                business_hour,
                test_sensor.get_number_visitor_error(
                    business_hour, business_day, business_month, business_year
                ),
            )
