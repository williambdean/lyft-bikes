"""Module to calculate pricing of divvy trips."""

import numpy as np
from dataclasses import dataclass


class Rate:
    """All pricing will derive from this class."""

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        """Calculate the rate for a given set of durations. Vectorized."""

    def __add__(self, other):
        return AdditiveRate(self, other)


class AdditiveRate(Rate):
    """A combination of two classes with addition."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        return self.left(duration=duration) + self.right(duration=duration)

    def __repr__(self) -> str:
        return f"AdditiveRate(left={self.left}, right={self.right})"


@dataclass
class MinuteRate(Rate):
    """Amount in cents per minute starting at `start` minute.

    Args:
        amount: the cost in cents per minute
        start: the minute where that cost starts

    Example:
        Rides that cost 15 cents per minute after 30 minutes of riding.

        ```python
        rate = MinuteRate(amount=15, start=30)
        rate([10, 15, 31]) # [0, 0, 16]
        ```

    """

    amount: int
    start: int

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        return np.maximum(np.rint(duration) - self.start, 0) * self.amount


@dataclass
class UnlockFee(Rate):
    """Amount in cents to unlock the bike."""

    amount: int

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        return np.ones_like(duration) * self.amount
