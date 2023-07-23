# Lyft Bike Share Data

Python client for Lyft bike share data.

All the information is derived from the official divvy bikes website: [https://divvybikes.com/](https://divvybikes.com/)

## Features 

- Support for [cities](https://www.lyft.com/bikes#cities) with Lyft bike share
- Historical trips 
- Live station and bike availability

## Installation 

Install from `pip` 

```shell 
$ pip install lyft-bikes
```

## Usage

### Reading Data

Reading from the various data sources can be done with the following functions.

```python 
import lyft_bikes

city = "Chicago"

# Historical trips between a given date range
df_trips = lyft_bikes.read_historical_trips(
    start_date="2021-01-01", 
    end_date="2021-02-01"
    city=city
)
# The trips from July 15th 2022 until latest
df_trips = lyft_bikes.read_historical_trips(start_date="2022-07-15", city=city)

# Available ebikes and scooters
df_available = lyft_bikes.read_available(city=city)

# Station information and bikes and scooters available there 
df_stations = divvy.read_stations(city=city)
```

### Trip Pricing

This package allows provides access to the latest pricing for the different bikes as defined [here](https://divvybikes.com/pricing). These prices can be apply to `pandas.Series` objects as follows: 

```python 
df_trips = pd.DataFrame({
    "duration_in_mins": [10, 10, 10, 10], 
    "member": [True, True, False, False], 
    "electric_bike": [True, False, True, False], 
})

df_trips["price"] = lyft_bikes.apply_pricing(
    duration=df_trips["duration_in_mins"], 
    member=df_trips["member"], 
    electric_bike=df_trips["electric_bike"], 
)
```

Classic bike prices for casual users are ambiguous due to the daily rate or single trip rate. However, they can be accessed in the `lyft_bikes.pricing` module as so. 

```python
casual_non_electric_duration = [10, 20, 30]

lyft_bikes.pricing.single_ride_rate(casual_non_electric_duration)
lyft_bikes.pricing.visitor_pass_rate(casual_non_electric_duration)
```

New pricing can easily be defined from the `divvy.pricing` module as well. For instance, a reduced ebike rate can be created for casual users. 

```python 
reduced_ebike_rate = (
    lyft_bikes.pricing.UnlockRate(amount=100) 
    + lyft_bikes.pricing.MinuteRate(amount=25, start=0)
)

casual_electric_duration = [10, 20, 30]

reduced_ebike_rate(casual_electric_duration)
```

## Development

The development environment was created with [`poetry`](https://python-poetry.org/docs/). The `pyproject.toml` file is the main configuration file for the project.

```bash
poetry install . 
```

## Contributing

If you would like to contribute or find some issue in the code, please [open an Issue](https://github.com/wd60622/divvy/issues/new) or a PR on GitHub. Thanks!