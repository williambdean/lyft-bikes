import pytest

from datetime import date

from divvy.historical.dates import DivvyDates, DateRangeError


@pytest.fixture
def divvy_dates():
    return DivvyDates()


@pytest.mark.parametrize(
    "start_date, end_date, answer",
    [
        ("2021-01-01", "2021-02-01", [date(2021, 1, 1), date(2021, 2, 1)]),
        ("2021-01-01", "2021-01-31", [date(2021, 1, 1)]),
        ("2021-01-01", "2021-01-01", [date(2021, 1, 1)]),
        # Doesn't produce list
        ("2021-02-01", "2021-01-01", []),
    ],
)
def test_date_range(divvy_dates, start_date, end_date, answer) -> None:
    result = divvy_dates.create_date_range(start_date, end_date)

    assert result == answer


@pytest.mark.parametrize(
    "date, answer",
    [
        ("2021-01-01", date(2021, 1, 1)),
        ("2021-01-31", date(2021, 1, 1)),
    ],
)
def test_first_of_month(divvy_dates, date, answer) -> None:
    assert divvy_dates.first_of_month(date) == answer
