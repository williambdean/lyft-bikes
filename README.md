# Divvy Rideshare Data

## Overview 

Access Chicago rideshare data from Python.

Data sources taken from here: https://ride.divvybikes.com/system-data 

Which come from: 

- Historical: https://divvy-tripdata.s3.amazonaws.com/index.html 
- Live and stations: https://gbfs.divvybikes.com/gbfs/gbfs.json

## Usage

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

## Installation 

Install from `pip` 

```shell 
$ pip install python-divvy
```