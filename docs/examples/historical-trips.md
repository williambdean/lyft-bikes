# Historical Trips

The `lyft_bikes` package provides access to historical trips for cities with Lyft bike share.

Read into a `pandas.DataFrame` with the `read_historical_trips` function.

```python
import lyft_bikes

city = "Chicago"
start_date = "2023-01-01"
end_date = "2023-01-31"

df_trips_chicago = lyft_bikes.read_historical_trips(
    start_date=start_date,
    end_date=end_date,
    city=city
)
```

```text
            ride_id  rideable_type           started_at             ended_at           start_station_name  ...  start_lat  start_lng    end_lat    end_lng  member_casual
0  F96D5A74A3E41399  electric_bike  2023-01-21 20:05:42  2023-01-21 20:16:33  Lincoln Ave & Fullerton Ave  ...  41.924074 -87.646278  41.930000 -87.640000         member
1  13CB7EB698CEDB88   classic_bike  2023-01-10 15:37:36  2023-01-10 15:46:05        Kimbark Ave & 53rd St  ...  41.799568 -87.594747  41.809835 -87.599383         member
2  BD88A2E670661CE5  electric_bike  2023-01-02 07:51:57  2023-01-02 08:05:11       Western Ave & Lunt Ave  ...  42.008571 -87.690483  42.039742 -87.699413         casual
3  C90792D034FED968   classic_bike  2023-01-22 10:52:58  2023-01-22 11:01:44        Kimbark Ave & 53rd St  ...  41.799568 -87.594747  41.809835 -87.599383         member
4  3397017529188E8A   classic_bike  2023-01-12 13:58:01  2023-01-12 14:13:20        Kimbark Ave & 53rd St  ...  41.799568 -87.594747  41.809835 -87.599383         member
```

Read the comparable data for New York City:

```python
city = "New York City"

df_trips_nyc = lyft_bikes.read_historical_trips(
    start_date=start_date,
    end_date=end_date,
    city=city
)
```

```text
            ride_id  rideable_type           started_at             ended_at                  start_station_name  ...  start_lat  start_lng    end_lat    end_lng  member_casual
0  4A86C1475DCCADA0   classic_bike  2023-01-26 10:53:44  2023-01-26 11:05:17               E 53 St & Madison Ave  ...  40.759724 -73.973664  40.777057 -73.978985         member
1  AE02E1FF7E264874   classic_bike  2023-01-04 11:51:54  2023-01-04 12:07:09               Halsey St & Ralph Ave  ...  40.684970 -73.922755  40.693261 -73.968896         casual
2  D3F9A2A71AD244C6   classic_bike  2023-01-04 17:26:48  2023-01-04 17:43:29                 Bank St & Hudson St  ...  40.736566 -74.006092  40.767272 -73.993929         casual
3  3D48C6F33AFEF329   classic_bike  2023-01-04 08:31:11  2023-01-04 08:42:12               E 53 St & Madison Ave  ...  40.759711 -73.974023  40.759291 -73.988597         member
4  4865926C3D97BA01  electric_bike  2023-01-03 22:15:34  2023-01-03 22:30:35  Frederick Douglass Blvd & W 112 St  ...  40.801694 -73.957145  40.765909 -73.976342         casual
```
