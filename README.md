# divvy

## Overview 

Chicago Divvy data from Python

Data sources taken from here: https://ride.divvybikes.com/system-data

Historical: https://divvy-tripdata.s3.amazonaws.com/index.html
Live and stations: https://gbfs.divvybikes.com/gbfs/gbfs.json

## Usage

```python 
from divvy.historical import HistoricalTrips 

trips = HistoricalTrips()
df_trips = trips.read(start_date="2021-01-01", end_date="2021-02-01")
```

```python 
from divvy.live import Live
live = Live()

df_available = live.read()
```

```python 
from divvy.stations import StationInfo, StationStatus

df_info = StationInfo().read()
df_status = StationStatus().read()
```