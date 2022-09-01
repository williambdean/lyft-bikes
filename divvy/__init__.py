import pandas as pd
import numpy as np

from typing import Union

from divvy.live import Live
from divvy.stations import StationInfo, StationStatus

from divvy.historical.dates import DivvyDates
from divvy.historical.historical import HistoricalTrips, Downloader

from divvy import pricing

from divvy.geo import read_fee_boundary

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


def read_historical_trips(
    start_date: str, end_date: Union[str, None] = None
) -> pd.DataFrame:
    """Read historical trips."""
    trips = HistoricalTrips(
        dates=DivvyDates(),
        downloader=Downloader(),
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
