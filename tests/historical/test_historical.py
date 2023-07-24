import pytest

import pandas as pd

from datetime import date

from lyft_bikes.historical.dates import DivvyDates, DateRangeError
from lyft_bikes.historical.historical import HistoricalTrips
from lyft_bikes.historical.downloader import DivvyDownloader as Downloader


@pytest.fixture
def downloader() -> Downloader:
    return Downloader()


@pytest.mark.parametrize(
    "date, file_name",
    [
        (date(2021, 1, 1), "202101-divvy-tripdata.csv"),
    ],
)
def test_downloader(downloader, date, file_name) -> None:
    assert downloader.file_name(date=date, suffix="csv") == file_name


@pytest.fixture
def historical_trips(test_data_dir) -> HistoricalTrips:
    class MockDownloader:
        def read(self, date: date) -> pd.DataFrame:
            file_path = test_data_dir / "sample_historical_trips.csv"

            return pd.read_csv(file_path)

    return HistoricalTrips(dates=DivvyDates(), downloader=MockDownloader())


def test_get_trips(historical_trips) -> None:
    df_results = historical_trips.get_months_trips(year=2021, month=1)

    assert isinstance(df_results, pd.DataFrame)
    assert len(df_results) == 15


@pytest.mark.parametrize(
    "year, month",
    [
        (2000, 1),
        (2100, 1),
    ],
)
def test_get_trips_out_of_range(historical_trips, year, month) -> None:
    with pytest.raises(DateRangeError):
        historical_trips.get_months_trips(year=year, month=month)


def test_read(historical_trips) -> None:
    df_results = historical_trips.read(start_date="2021-01-01", end_date="2021-01-15")

    assert isinstance(df_results, pd.DataFrame)
    assert len(df_results) < 15
