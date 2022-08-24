import numpy as np

from divvy import pricing


def test_unlock() -> None:
    duration = np.array([1, 2, 3, 5, 6])

    amount = 100
    unlock = pricing.UnlockRate(amount=amount)
    result = unlock(duration=duration)

    answer = np.ones_like(duration) * amount

    assert np.all(answer == result)


def test_minute_rate() -> None:
    duration = np.array([1, 2, 3, 4, 5, 6])

    amount = 100
    wait = 3
    minute_rate = pricing.MinuteRate(amount=amount, start=wait)
    result = minute_rate(duration=duration)

    answer = np.array([0, 0, 0, 100, 200, 300])

    assert np.all(answer == result)


def test_unlock_minute_rate() -> None:
    duration = np.array([1, 2, 3, 4, 5, 6])

    amount = 100
    wait = 3
    rate = pricing.UnlockRate(amount=amount) + pricing.MinuteRate(
        amount=amount, start=wait
    )
    result = rate(duration=duration)

    answer = np.array([amount, amount, amount, amount * 2, amount * 3, amount * 4])

    assert np.all(answer == result)
