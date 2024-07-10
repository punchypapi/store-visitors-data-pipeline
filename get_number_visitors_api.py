from datetime import date

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.utils import create_sensor_data

app = FastAPI()
sensor_data = pd.DataFrame.from_dict(create_sensor_data())


def filter_sensor_dataframe(
    df: pd.DataFrame,
    filter_store: str,
    filter_id: int,
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
        (df.store == filter_store)
        & (df.id == filter_id)
        & (df.year == filter_year)
        & (df.month == filter_month)
        & (df.day == filter_day)
        & (df.hour == filter_hour)
    ]
    return int(filtered_df["visitors"].values[0])


@app.get("/")
def get_number_visitor(
    selected_store: str,
    selected_id: int,
    selected_day: int,
    selected_month: int,
    selected_year: int,
    selected_hour: str | None = None,
) -> JSONResponse:
    """
    Retrieve number of visitor captured by the sensor
    for a given datetime

    """
    # check store selected
    if selected_store not in tuple(sensor_data["store"]):
        return JSONResponse(
            status_code=404,
            content="Enter a valid store, list of valid stores : Lille, Paris, Toulouse",
        )
    # check captor id selected
    if not (selected_id <= 3 and selected_id >= 1):
        return JSONResponse(
            status_code=404, content="Please select a sensor id between 1 and 3"
        )
    # return error if year selected is not available
    if selected_year < 2021 or selected_year > 2024:
        return JSONResponse(
            status_code=404,
            content="No data available for the selected year, please select year between 2021 and 2024",
        )
    # check date validity
    else:
        try:
            date(selected_year, selected_month, selected_day)
        except ValueError:
            return JSONResponse(status_code=404, content="Enter a valid date")

        if selected_hour is None:
            default_hour = "12:00"
            number_visitors = filter_sensor_dataframe(
                sensor_data,
                selected_store,
                selected_id,
                selected_day,
                selected_month,
                selected_year,
                default_hour,
            )
        else:
            number_visitors = filter_sensor_dataframe(
                sensor_data,
                selected_store,
                selected_id,
                selected_day,
                selected_month,
                selected_year,
                selected_hour,
            )

        return JSONResponse(status_code=200, content=number_visitors)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


# curl -v "http://0.0.0.0:8080/?selected_store=Lille&selected_id=3&selected_day=8&selected_month=5&selected_year=2024&selected_hour=10:00"
