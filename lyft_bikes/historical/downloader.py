import datetime 
import io
import requests 
import zipfile 

import pandas as pd

from lyft_bikes.divvy_request import BadRequest


class BaseDownloader:
    def __init__(self, http_client=requests) -> None:
        self.http_client = http_client

    def file_name(self, date: datetime.date, suffix: str) -> str:
        raise NotImplementedError("This method should be implemented in the child class.")
    
    @property 
    def base_url(self) -> str:
        raise NotImplementedError("This method should be implemented in the child class.")
    
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
        return f"{date:%Y%m}-citibike-tripdata.{suffix}"

    def url(self, date: datetime.date):
        return f"{self.base_url}/{self.file_name(date=date, suffix='csv.zip')}"
    

if __name__ == "__main__": 
    citi_bikes = CitiBikesDownloader()

    df = citi_bikes.read(date=datetime.date(2023, 6, 1))