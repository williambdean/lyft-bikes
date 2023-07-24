"""Access the live feed of bikes and scooters. More to come."""
from lyft_bikes.live import LiveRequest


class Bikes(LiveRequest):
    """Fetch the live feed of bikes and scooters.

    Example:
        Get the live ebikes and scooters as pandas.DataFrame

        ```python
        live_bikes = Bikes()
        df_live_bikes = live_bikes.read()
        ```

    """

    url: str = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
    key: str = "bikes"
