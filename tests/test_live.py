import pytest

from lyft_bikes.live import RequestBase, LiveRequest


@pytest.fixture
def new_source():
    class NewDivvyData(LiveRequest):
        pass

    return NewDivvyData()


def test_default(new_source):
    assert isinstance(new_source.requests_base, RequestBase)
