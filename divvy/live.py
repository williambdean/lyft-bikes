from divvy.divvy_request import DivvyDataBase


class Live(DivvyDataBase):
    """Live feed endpoint.

    Access ebikes and scooters that are currently available.

    Example:
        Get the live ebikes and scooters as pandas.DataFrame

        >>> live = Live()
        >>> df_live = live.read()

    """

    url: str = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
    key: str = "bikes"
