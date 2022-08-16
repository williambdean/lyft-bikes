from divvy.divvy_request import DivvyDataBase


class StationBase(DivvyDataBase):
    key: str = "stations"


class StationInfo(StationBase):
    url: str = "https://gbfs.divvybikes.com/gbfs/en/station_information.json"


class StationStatus(StationBase):
    url: str = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
