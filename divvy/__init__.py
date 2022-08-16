import pandas as pd
import geopandas as gpd

from typing import Union

from divvy.live import Live
from divvy.stations import StationInfo, StationStatus
from divvy.historical.dates import DivvyDates
from divvy.historical.historical import HistoricalTrips, Downloader

__version__ = "0.0.1"


def read_live() -> pd.DataFrame:
    live = Live()
    return live.read()


def read_stations() -> pd.DataFrame:
    station_info = StationInfo()
    station_status = StationStatus()

    return pd.merge(
        station_status.read(),
        station_info.read(),
        how="inner",
        on=["station_id", "legacy_id"],
    )


def read_historical_trips(
    start_date: str, end_date: Union[str, None] = None
) -> pd.DataFrame:
    trips = HistoricalTrips(
        dates=DivvyDates(),
        downloader=Downloader(),
    )

    return trips.read(start_date=start_date, end_date=end_date)
