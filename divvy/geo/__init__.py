from pathlib import Path

try:
    import geopandas as gpd
except ImportError:
    gpd = None


def read_fee_boundary() -> "GeoDataFrame":
    """Read in the fee boundary before the pricing change in May 2022.

    Polygon created by referencing the divvy site and using online software
    to create custom map: https://www.keene.edu/campus/maps/tool/

    Returns:
        GeoDataFrame with single row geometry

    """
    if gpd is None:
        msg = "The package 'geopandas' must be installed to read fee boundary."
        raise ImportError(msg)

    file = Path(__file__).parent / "fees.geojson"

    return gpd.read_file(file, crs="EPSG:4326")
