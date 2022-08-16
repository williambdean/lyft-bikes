import pytest

from divvy.divvy_request import RequestBase, DivvyDataBase


@pytest.fixture
@pytest.fixture
def new_source():
    class NewDivvyData(DivvyDataBase):
        pass

    return NewDivvyData()


def test_default(new_source):
    assert isinstance(new_source.requests_base, RequestBase)
