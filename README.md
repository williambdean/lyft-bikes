# divvy

## Overview 

Chicago Divvy data from Python

Data sources taken from here: https://ride.divvybikes.com/system-data

Historical: https://divvy-tripdata.s3.amazonaws.com/index.html
Live and stations: https://gbfs.divvybikes.com/gbfs/gbfs.json

## Usage

```python 
import divvy

# Historical trips 
df_trips = divvy.read_historical_trips(start_date="2021-01-01", end_date="2021-02-01")

# Available ebikes and scooters
df_available = divvy.read_available()

# Station information and bikes and scooters available there 
df_stations = divvy.read_stations()
```