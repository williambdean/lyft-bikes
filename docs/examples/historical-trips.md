# Historical Trips

The Divvy system has been around since 2013 and has been collecting data on every trip since then. This data is available for download from the [Divvy Data Portal](https://www.divvybikes.com/system-data).

The data is available in monthly CSV files, which can be downloaded and read into a `pandas.DataFrame` with the `read_historical_trips` function. 

```python
import lyft_bikes

city = "Chicago"

df_trips = lyft_bikes.read_historical_trips(
    start_date="2021-01-01", 
    end_date="2021-02-01", 
    city=city
)
```
