from src.sensor import Sensor
import unittest
from datetime import date


class TestSensor(unittest.TestCase):
    def test_visitors_closing_hours(self):
        """
        Test to check that the Sensor visitor generator
        returns 0 visitors during closing hours

        """
        test_sensor = Sensor(0.2, 3000, 100)
        hour_range = [f"0{i}:00" for i in range(10)] + [
            f"{i}:00" for i in range(10, 24)
        ]
        business_day, business_month, business_year = (4, 7, 2024)
        for business_hour in hour_range:
            if business_hour > "19:00" or business_hour < "09:00":
                number_visitors = test_sensor.get_number_visitor_error(
                    business_hour, business_day, business_month, business_year
                )
                self.assertEqual(
                    number_visitors, 0, "error implementing closing hour rule"
                )

    def test_visitors_sundays(self):
        """
        Test to check that the Sensor visitor generator
        returns 0 visitors during closing days (Sundays)

        """
        test_sensor = Sensor(0.2, 3000, 100)
        day_range = [i for i in range(1, 30)]
        business_hour, business_month, business_year = ("12:00", 9, 2024)
        for business_day in day_range:
            business_date = date(business_year, business_month, business_day)
            day_of_the_week = business_date.weekday()
            if day_of_the_week == 6:
                number_visitors = test_sensor.get_number_visitor_error(
                    business_hour, business_day, business_month, business_year
                )
                self.assertEqual(
                    number_visitors, 0, "error implementing closing days rule"
                )

    def test_visitors_august(self):
        """
        Test to check that the Sensor visitor generator
        returns 0 visitors during closing days (August)

        """
        test_sensor = Sensor(0.2, 3000, 100)
        day_range = [i for i in range(1, 32)]
        business_hour, business_month, business_year = ("12:00", 8, 2024)
        for business_day in day_range:
            number_visitors = test_sensor.get_number_visitor_error(
                business_hour, business_day, business_month, business_year
            )
            self.assertEqual(number_visitors, 0, "error implementing closing days rule")

    def test_sensor_error(self):
        """
        Test to check that sensors take into account errors due to malfunctioning,
        Expect at least one outlier on a yearly records of year number of visitors
        """
        records = 0
        records_containing_errors = 0
        test_sensor = Sensor(0.2, 3000, 100)
        opening_hour_range = ["09:00"] + [f"{i}:00" for i in range(10, 20)]
        day_range = [i for i in range(1, 32)]
        business_hour, business_month, business_year = ("12:00", 10, 2024)
        for business_day in day_range:
            business_date = date(business_year, business_month, business_day)
            day_of_the_week = business_date.weekday()
            if day_of_the_week != 6:
                for business_hour in opening_hour_range:
                    records += 1
                    number_visitors = test_sensor.get_number_visitor_error(
                        business_hour, business_day, business_month, business_year
                    )
                    print(number_visitors)
                    if number_visitors <= 700:
                        records_containing_errors += 1
        error_percentage = records_containing_errors / records
        self.assertGreaterEqual(error_percentage, 0.05)


if __name__ == "__main__":
    unittest.main()
