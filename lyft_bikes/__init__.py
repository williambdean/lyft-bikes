import pandas as pd

from functools import wraps
from typing import Dict, Union

from lyft_bikes.bikes import Bikes
from lyft_bikes.stations import StationInfo, StationStatus

from lyft_bikes.historical.historical import HistoricalTrips
from lyft_bikes.historical import dates as bike_dates, downloader

from lyft_bikes.geo import read_fee_boundary

__version__ = "0.1.2"


def chicago_only_error(func) -> None:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get("city") != "Chicago" or args[0] != "Chicago":
            raise ValueError(f"{func.__name__} is only available for Chicago.")

        return func(*args, **kwargs)

    return wrapper


@chicago_only_error
def read_live_bikes(city: str) -> pd.DataFrame:
    """Read currently available bikes and scooters.

    Args:
        city: city to read data from

    Returns:
        DataFrame with the current status of bikes and scooters.

    """
    live = Bikes()
    return live.read()


@chicago_only_error
def read_stations(city: str) -> pd.DataFrame:
    """Read information and status for each station.

    Args:
        city: city to read data from

    Returns:
        DataFrame with the stations information and status.

    """
    station_info = StationInfo()
    station_status = StationStatus()

    return pd.merge(
        station_status.read(),
        station_info.read(),
        how="inner",
        on=["station_id", "legacy_id"],
    )


CITY_DATES: Dict[str, bike_dates.DefaultDates] = {
    "Chicago": bike_dates.DivvyDates,
}


CITY_DOWNLOADERS: Dict[str, downloader.BaseDownloader] = {
    "Chicago": downloader.DivvyDownloader,
    "New York City": downloader.CitiBikesDownloader,
    "San Francisco": downloader.BayWheelsDownloader,
    "Washington DC": downloader.CapitalBikeshareDownloader,
    "Columbus": downloader.CoGoDownloader,
}


def read_historical_trips(
    start_date: str,
    city: str,
    end_date: Union[str, None] = None,
) -> pd.DataFrame:
    """Read historical trips within given range of dates for a city.

    Args:
        start_date: start date for the data in %Y-%m-%d format
        city: city to read data from
        end_date: end date in the same format. Defaults to last date available

    Returns:
        Historical trip DataFrame for the date range provided.

    Examples:
        Read trips from Jan 1st 2021 until Feb 1st 2021 in Chicago

        ```python
        import lyft_bikes

        df = lyft_bikes.read_historical_trips(
            start_date="2021-01-01",
            end_date="2021-02-01",
            city="Chicago",
        )
        ```


    """
    if city not in CITY_DOWNLOADERS:
        raise ValueError(
            f"City {city} is not supported. Supported cities are {CITY_DOWNLOADERS.keys()}"
        )

    dates = CITY_DATES.get(city, bike_dates.DefaultDates)()

    downloader = CITY_DOWNLOADERS[city]()
    trips = HistoricalTrips(
        dates=dates,
        downloader=downloader,
    )
    return trips.read(start_date=start_date, end_date=end_date)
