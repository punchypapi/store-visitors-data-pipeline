from datetime import date

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src import create_sensor_data

app = FastAPI()
sensor_data = pd.DataFrame.from_dict(create_sensor_data())


def filter_sensor_dataframe(
    df: pd.DataFrame,
    filter_day: int,
    filter_month: int,
    filter_year: int,
    filter_hour: str,
) -> int:
    """
    Apply a datetime filters to
    retrieve number of visitor captured by the sensor

    """
    filtered_df = df[
        (df.year == filter_year)
        & (df.month == filter_month)
        & (df.day == filter_day)
        & (df.hour == filter_hour)
    ]
    return int(filtered_df["visitors"].values[0])


@app.get("/")
def get_number_visitor(
    day: int, month: int, year: int, hour: str | None = None
) -> JSONResponse:
    """
    Retrieve number of visitor captured by the sensor
    for a given datetime

    """
    # return error if year < 2021
    if year < 2021 or year > 2024:
        return JSONResponse(status_code=404, content="Not data for the year inputed")
    # check date validity
    else:
        try:
            date(year, month, day)
        except ValueError:
            return JSONResponse(status_code=404, content="Enter a valid date")

        if hour is None:
            default_hour = "12:00"
            number_visitors = filter_sensor_dataframe(
                sensor_data, day, month, year, default_hour
            )
        else:
            number_visitors = filter_sensor_dataframe(
                sensor_data, day, month, year, hour
            )

        return JSONResponse(status_code=200, content=number_visitors)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# curl -v "http://0.0.0.0:8000/?day=18&month=01&year=2023&hour="20:00""
