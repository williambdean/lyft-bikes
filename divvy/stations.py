from divvy.divvy_request import RequestBase


class StationBase(RequestBase):
    key: str = "stations"


class StationInfo(StationBase):
    url: str = "https://gbfs.divvybikes.com/gbfs/en/station_information.json"


class StationStatus(StationBase):
    url: str = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"


if __name__ == "__main__":
    df_info = StationInfo().read()
    df_status = StationStatus().read()
