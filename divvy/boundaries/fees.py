"""The old boundary for free ebikes with the membership."""
import geopandas as gpd

from pathlib import Path


HERE = Path(__file__).parent


def read_boundary() -> gpd.GeoDataFrame:
    file = HERE / "fees.geojson"

    return gpd.read_file(file)
