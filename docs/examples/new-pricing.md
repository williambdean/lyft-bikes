# New Prices

Prices can be created by adding together `UnlockFee` and `MinuteRate` objects. The `UnlockFee` is a one-time fee charged at the start of the trip. The `MinuteRate` is the price per minute after the first `start` minutes.

```python 
pricing = UnlockFee(unlock_fee) + MinuteRate(minute_rate, start=start_minute)
```

A pricing instance can be called with a number of minutes to get the total price for a trip of that length.

```python
pricing(minutes)
```

Below is an example of comparing two different pricing schemes.

```python
import numpy as np

import matplotlib.pyplot as plt

from lyft_bikes.pricing import UnlockFee, MinuteRate

pricing_1 = UnlockFee(0.5) + MinuteRate(0.10, start=30)
pricing_2 = UnlockFee(1.0) + MinuteRate(0.05, start=30)

minutes = np.arange(0, 90)

ax = plt.gca()
ax.plot(minutes, pricing_1(minutes), label="Pricing 1")
ax.plot(minutes, pricing_2(minutes), label="Pricing 2")
ax.set_ylim(0, None)
ax.set(
    title="Pricing Comparison",
    xlabel="Minutes",
    ylabel="Price ($)",
)
plt.legend()
plt.show()
```

![png](./../images/pricing.png)