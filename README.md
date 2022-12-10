# Divvy Rideshare Data

## Overview 

Access and work with Chicago rideshare data from Python.

All the information is derived from the official divvy bikes website: https://divvybikes.com/

Where the data sources were linked to: https://ride.divvybikes.com/system-data 

which point to: 

- Historical: https://divvy-tripdata.s3.amazonaws.com/index.html 
- Live and stations: https://gbfs.divvybikes.com/gbfs/gbfs.json


## Installation 

Install from `pip` 

```shell 
$ pip install python-divvy
```

## Usage

### Reading Data

Reading from the various data sources can be done with the following functions.

```python 
import divvy

# Historical trips between a given date range
df_trips = divvy.read_historical_trips(
    start_date="2021-01-01", 
    end_date="2021-02-01"
)
# The trips from July 15th 2022 until latest
df_trips = divvy.read_historical_trips(start_date="2022-07-15")

# Available ebikes and scooters
df_available = divvy.read_available()

# Station information and bikes and scooters available there 
df_stations = divvy.read_stations()
```

With the install of [`geopandas`](https://geopandas.org/en/stable/), the pre-May 2022 pricing boundary for ebikes can be accessed with the `read_fee_boundary` function. 

```python 
# Single row geopandas.GeoDataFrame
gdf_fees = divvy.read_fee_boundary()
```

### Trip Pricing

This package allows provides access to the latest pricing for the different bikes as defined [here](https://divvybikes.com/pricing). These prices can be apply to `pandas.Series` objects as follows: 

```python 
df_trips = pd.DataFrame({
    "duration_in_mins": [10, 10, 10, 10], 
    "member": [True, True, False, False], 
    "electric_bike": [True, False, True, False], 
})

df_trips["price"] = divvy.apply_pricing(
    duration=df_trips["duration_in_mins"], 
    member=df_trips["member"], 
    electric_bike=df_trips["electric_bike"], 
)
```

Classic bike prices for casual users are ambiguous due to the daily rate or single trip rate. However, they can be accessed in the `divvy.pricing` module as so. 

```python
casual_non_electric_duration = [10, 20, 30]

divvy.pricing.single_ride_rate(casual_non_electric_duration)
divvy.pricing.visitor_pass_rate(casual_non_electric_duration)
```

New pricing can easily be defined from the `divvy.pricing` module as well. For instance, a reduced ebike rate can be created for casual users. 

```python 
reduced_ebike_rate = (
    divvy.pricing.UnlockRate(amount=100) 
    + divvy.pricing.MinuteRate(amount=25, start=0)
)

casual_electric_duration = [10, 20, 30]

reduced_ebike_rate(casual_electric_duration)
```

## Development

The development environment was created with `conda` and can be recreated and activated that way. Here are some helpful commands for [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

If there is a change to dependencies in the project, the `setup.py` will likely have to be changed as well.

The `setup.py` is important for deployment to PyPI. The project might move to another package manager in the future. In order to ease deployment.

## Contributing

If you would like to contribute or find some issue in the code, please [open an Issue](https://github.com/wd60622/divvy/issues/new) or a PR on GitHub. Thanks!