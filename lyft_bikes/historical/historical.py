import pandas as pd

from typing import Union

from lyft_bikes.historical.dates import DivvyDates
from lyft_bikes.historical.downloader import BaseDownloader


class HistoricalTrips:
    def __init__(self, dates: DivvyDates, downloader: BaseDownloader):
        self.dates = dates
        self.downloader = downloader

    def read(self, start_date: str, end_date: Union[str, None] = None) -> pd.DataFrame:
        """Return historical trips for a given range of dates

        Args:
            start_date: start date for the data in %Y-%m-%d format
            end_date: end date in the same format. Defaults to last date available

        Returns:
            Historical trip DataFrame for the date range provided.

        Examples:
            Read trips from Jan 1st 2021 until Feb 1st 2021

            >>> trips = HistoricalTrips()
            >>> df_trips = trips.read(start_date="2021-01-01", end_date="2021-02-01")

            Read trips from Jan 1st 2021 on

            >>> df_trips = trips.read(start_date="2021-01-01")

        """
        if end_date is None:
            end_date = str(self.dates.last_date)

        df_trips = pd.concat(
            [
                self.get_trips(date.year, date.month)
                for date in self.dates.create_date_range(start_date, end_date)
            ],
            ignore_index=True,
        )

        date = pd.to_datetime(df_trips["started_at"]).dt.date.astype(str)
        idx = (date >= start_date) & (date <= end_date)
        return df_trips.loc[idx, :].reset_index(drop=True)

    def get_trips(self, year: int, month: int) -> pd.DataFrame:
        """Return pandas.DataFrame for a given year and month"""
        date = self.dates.to_date(year, month)
        self.dates.check_valid(date)

        return self.downloader.read(date=date)
