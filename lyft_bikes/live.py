import pandas as pd

from typing import Dict

import requests
import json

import datetime


class BadRequest(Exception):
    """Some error happened with the request."""


class RequestBase:
    """Base for getting data sources from Divvy gbfs.

    Get a JSON data source from url and cache it

    """

    def __init__(self) -> None:
        self._data = None

    def data(self, url: str) -> Dict:
        if self._data is not None:
            return self._data

        response = requests.get(url)

        if not response.ok:
            raise BadRequest(f"The response to {url} was not ok. {response.text}")

        return json.loads(response.text)


class LiveRequest(RequestBase):
    key: str = None
    url: str = None

    def __init__(self, requests_base: RequestBase = None) -> None:
        if requests_base is None:
            requests_base = RequestBase()

        self.requests_base = requests_base

    @property
    def data(self) -> Dict:
        return self.requests_base.data(self.url)

    @property
    def last_updated(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.data["last_updated"])

    def read(self) -> pd.DataFrame:
        return pd.DataFrame(self.data["data"][self.key])
