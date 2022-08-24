"""Module to calculate pricing of divvy trips.

As defined here: https://divvybikes.com/pricing

Comprised of an unlock and 

"""
import numpy as np
from dataclasses import dataclass


class Rate:
    def __call__(self, duration: np.ndarray) -> np.ndarray:
        """Calculate the rate for a given set of durations. Vectorized."""

    def __add__(self, other):
        return AdditiveRate(self, other)


class AdditiveRate(Rate):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        return self.left(duration=duration) + self.right(duration=duration)

    def __repr__(self) -> str:
        return f"AdditiveRate(left={self.left}, right={self.right})"


@dataclass
class MinuteRate(Rate):
    """Amount in cents per minute starting at `start` minute."""

    amount: int
    start: int

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        return np.maximum(np.rint(duration) - self.start, 0) * self.amount


@dataclass
class UnlockRate(Rate):
    """Amount in cents to unlock the bike."""

    amount: int

    def __call__(self, duration: np.ndarray) -> np.ndarray:
        return np.ones_like(duration) * self.amount


# Classic Bikes
member_classic_rate = MinuteRate(amount=16, start=45)
single_ride_rate = UnlockRate(amount=100) + MinuteRate(amount=16, start=0)
visitor_pass_rate = MinuteRate(amount=16, start=3 * 60)

# Ebikes
member_ebike_rate = MinuteRate(amount=16, start=0)
casual_ebike_rate = UnlockRate(amount=100) + MinuteRate(amount=39, start=0)
