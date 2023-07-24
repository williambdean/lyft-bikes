"""Access station information and status. More to come."""
from lyft_bikes.live import LiveRequest


class StationBase(LiveRequest):
    key: str = "stations"


class StationInfo(StationBase):
    url: str = "https://gbfs.divvybikes.com/gbfs/en/station_information.json"


class StationStatus(StationBase):
    url: str = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
