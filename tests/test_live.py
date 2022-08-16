import pytest

import pandas as pd

import json
from typing import Dict

from divvy.live import Live


@pytest.fixture
def live(test_data_dir) -> Live:
    class RequestBaseMock:
        def data(self, url: str) -> Dict:
            file = test_data_dir / "fake-live-feed.json"
            with open(file, "r") as f:
                data = json.load(f)

            return data

    return Live(requests_base=RequestBaseMock())


def test_read(live) -> None:
    df_results = live.read()

    assert isinstance(df_results, pd.DataFrame)
    assert len(df_results) == 5
