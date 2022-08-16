import pytest

import pandas as pd

from divvy.stations import StationStatus, StationInfo


@pytest.fixture
def info(mock_requests_base) -> StationInfo:
    mock_requests_base.file_name = "fake-station-info.json"

    return StationInfo(requests_base=mock_requests_base)


@pytest.fixture
def status(mock_requests_base) -> StationStatus:
    mock_requests_base.file_name = "fake-station-status.json"

    return StationStatus(requests_base=mock_requests_base)


@pytest.mark.parametrize(
    "fixture_name, n_stations",
    [
        ("info", 5),
        ("status", 5),
    ],
)
def test_stations(fixture_name, n_stations, request) -> None:
    fixture = request.getfixturevalue(fixture_name)

    df_results = fixture.read()

    assert isinstance(df_results, pd.DataFrame)
    assert len(df_results) == n_stations
