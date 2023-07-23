import pandas as pd
import numpy as np

from typing import Union

from lyft_bikes.live import Live
from lyft_bikes.stations import StationInfo, StationStatus

from lyft_bikes.historical.dates import DivvyDates
from lyft_bikes.historical.historical import HistoricalTrips
from lyft_bikes.historical import downloader

from lyft_bikes import pricing

from lyft_bikes.geo import read_fee_boundary

__version__ = "0.0.5"


def read_live() -> pd.DataFrame:
    """Read currently available bikes and scooters."""
    live = Live()
    return live.read()


def read_stations() -> pd.DataFrame:
    """Read information and status for each station."""
    station_info = StationInfo()
    station_status = StationStatus()

    return pd.merge(
        station_status.read(),
        station_info.read(),
        how="inner",
        on=["station_id", "legacy_id"],
    )


CITY_DOWNLOADERS = {
    "Chicago": downloader.DivvyDownloader, 
    "New York City": downloader.CitiBikesDownloader,
}

def read_historical_trips(
    start_date: str, city: str, end_date: Union[str, None] = None, 
) -> pd.DataFrame:
    """Read historical trips."""
    if city not in CITY_DOWNLOADERS:
        raise ValueError(f"City {city} is not supported. Supported cities are {CITY_DOWNLOADERS.keys()}")
    
    downloader = CITY_DOWNLOADERS[city]()
    trips = HistoricalTrips(
        dates=DivvyDates(),
        downloader=downloader, 
    )

    return trips.read(start_date=start_date, end_date=end_date)


def apply_pricing(
    duration: pd.Series, member: pd.Series, electric_bike: pd.Series
) -> pd.Series:
    """Applying trip level pricing.

    Currently doesn't assume the classic bike pricing for casual users as the
    price could be ambiguous.

    Args:
        duration: duration of the trip in minutes
        member: boolean indication of membership. member = 1
        electric_bike: boolean indication of electric bike: electric bike = 1

    Returns:
        series of the price in cents for the trips

    """
    # Initialize null values
    result = pd.Series(np.nan, index=duration.index)

    idx = member & electric_bike
    result.loc[idx] = pricing.member_ebike_rate(duration.loc[idx])

    idx = member & ~electric_bike
    result.loc[idx] = pricing.member_classic_rate(duration.loc[idx])

    idx = ~member & electric_bike
    result.loc[idx] = pricing.casual_ebike_rate(duration.loc[idx])

    return result
