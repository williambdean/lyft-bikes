import datetime
import io
import requests
import zipfile

import pandas as pd

from lyft_bikes.live import BadRequest


class BaseDownloader:
    def __init__(self, http_client=requests) -> None:
        self.http_client = http_client

    def file_name(self, date: datetime.date, suffix: str) -> str:
        raise NotImplementedError(
            "This method should be implemented in the child class."
        )

    @property
    def base_url(self) -> str:
        raise NotImplementedError(
            "This method should be implemented in the child class."
        )

    def url(self, date: datetime.date):
        return f"{self.base_url}/{self.file_name(date=date, suffix='zip')}"

    def read(self, date: datetime.date) -> pd.DataFrame:
        url = self.url(date=date)
        response = self.http_client.get(url)

        if not response.ok:
            raise BadRequest(f"The response for {url} wasn't okay.")

        zipdata = zipfile.ZipFile(io.BytesIO(response.content))

        return pd.read_csv(zipdata.open(self.file_name(date=date, suffix="csv")))


class DivvyDownloader(BaseDownloader):
    """Class to download historical trips from Divvy in Chicago.

    Index for all the historical trips found <a href="https://divvy-tripdata.s3.amazonaws.com/index.html">here</a>.

    Currently only supports the files with the form `%Y%m-divvy-tripdata.zip` that go back until
    April 2020

    """

    base_url = "https://divvy-tripdata.s3.amazonaws.com"

    def file_name(self, date: datetime.date, suffix: str) -> str:
        return f"{date:%Y%m}-divvy-tripdata.{suffix}"


class CitiBikesDownloader(BaseDownloader):
    """Class to download historical trips from CitiBikes in New York City.

    Index for all the historical trips found <a href="https://s3.amazonaws.com/tripdata/index.html">here</a>.

    """

    base_url = "https://s3.amazonaws.com/tripdata"

    def file_name(self, date: datetime.date, suffix: str) -> str:
        return f"JC-{date:%Y%m}-citibike-tripdata.{suffix}"

    def url(self, date: datetime.date):
        return f"{self.base_url}/{self.file_name(date=date, suffix='csv.zip')}"


class BayWheelsDownloader(BaseDownloader):
    """Class to download historical trips from BayBikes in San Francisco.

    Index for all the historical trips found <a href="https://s3.amazonaws.com/baywheels-data/index.html">here</a>.

    """

    base_url = "https://s3.amazonaws.com/baywheels-data"

    def file_name(self, date: datetime.date, suffix: str) -> str:
        return f"{date:%Y%m}-baywheels-tripdata.{suffix}"

    def url(self, date: datetime.date):
        return f"{self.base_url}/{self.file_name(date=date, suffix='csv.zip')}"


class CoGoDownloader(BaseDownloader):
    """Class to download historical trips from CoGo in Columbus.

    Index for all the historical trips found <a href="https://cogo-sys-data.s3.amazonaws.com/index.html">here</a>.

    """

    base_url = "https://cogo-sys-data.s3.amazonaws.com"

    def file_name(self, date: datetime.date, suffix: str) -> str:
        return f"{date:%Y%m}-cogo-tripdata.{suffix}"


class CapitalBikeshareDownloader(BaseDownloader):
    """Class to download historical trips from Capital Bikeshare in Washington DC.

    Index for all the historical trips found <a href="https://s3.amazonaws.com/capitalbikeshare-data/index.html">here</a>.

    """

    base_url = "https://s3.amazonaws.com/capitalbikeshare-data"

    def file_name(self, date: datetime.date, suffix: str) -> str:
        return f"{date:%Y%m}-capitalbikeshare-tripdata.{suffix}"
