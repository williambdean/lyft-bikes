import pandas as pd

from typing import Union, Dict

import requests
import json

import datetime


class BadRequest(Exception):
    """Some error happened with the request."""


class RequestBase:
    """Base for all data sources from Divvy"""

    key: str = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    @property
    def data(self) -> Dict:
        if not hasattr(self, "_data"):
            self._data = self.get_data()

        return self._data

    def get_data(self) -> Dict:
        response = requests.get(self.url)

        if not response.ok:
            raise BadRequest(f"The response to {self.url} was not ok. {response.text}")

        return json.loads(response.text)

    @property
    def last_updated(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.data["last_updated"])

    def read(self) -> pd.DataFrame:
        return pd.DataFrame(self.data["data"][self.key])
