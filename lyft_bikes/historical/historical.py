from datetime import date
from typing import Protocol, Union
import warnings

import pandas as pd


class Dates(Protocol):
    @property
    def last_date(self) -> date: ...

    def create_date_range(self, start_date: str, end_date: str) -> pd.Series: ...

    def to_date(self, year: int, month: int) -> date: ...

    def check_valid(self, date: date) -> None: ...


class Downloader(Protocol):
    def read(self, date: date) -> pd.DataFrame: ...


class HistoricalTrips:
    def __init__(self, dates: Dates, downloader: Downloader):
        self.dates = dates
        self.downloader = downloader

    def get_months_trips(self, year: int, month: int) -> pd.DataFrame:
        """Return pandas.DataFrame for a given year and month"""
        date = self.dates.to_date(year, month)
        self.dates.check_valid(date)

        return self.downloader.read(date=date)

    def read(
        self,
        start_date: str,
        start_time_col: str = "started_at",
        end_date: Union[str, None] = None,
    ) -> pd.DataFrame:
        """Return historical trips for a given range of dates

        Args:
            start_date: start date for the data in %Y-%m-%d format
            start_col_col: column name for the start time
            end_date: end date in the same format. Defaults to last date available

        Returns:
            Historical trip DataFrame for the date range provided.

        Examples:
            Read trips from Jan 1st 2021 until Feb 1st 2021

            >>> trips = HistoricalTrips()
            >>> df_trips = trips.read(start_date="2021-01-01", end_date="2021-02-01")

            Read trips from Jan 1st 2021 until the last date available

            >>> df_trips = trips.read(start_date="2021-01-01")

        """
        if end_date is None:
            end_date = str(self.dates.last_date)

        df_trips = pd.concat(
            [
                self.get_months_trips(date.year, date.month)
                for date in self.dates.create_date_range(start_date, end_date)
            ],
            ignore_index=True,
        )

        try:
            date = pd.to_datetime(df_trips[start_time_col]).dt.date.astype(str)
            idx = (date >= start_date) & (date <= end_date)
            return df_trips.loc[idx, :].reset_index(drop=True)
        except KeyError:
            warnings.warn(
                f"The column {start_time_col} does not exist. Returning all trips instead.",
                UserWarning,
            )
            return df_trips
