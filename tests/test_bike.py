from datetime import datetime
import pytest

import pandas as pd

from lyft_bikes.bikes import Bikes


@pytest.fixture
def live(mock_requests_base) -> Bikes:
    mock_requests_base.file_name = "fake-live-feed.json"

    return Bikes(requests_base=mock_requests_base)


def test_read(live) -> None:
    df_results = live.read()

    assert isinstance(df_results, pd.DataFrame)
    assert len(df_results) == 5
    assert isinstance(live.last_updated, datetime)
