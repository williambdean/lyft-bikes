import pandas as pd
import numpy as np

import lyft_bikes


def test_apply_pricing():
    df = pd.DataFrame(
        {
            "duration": [5, 5, 5, 5],
            "casual_member": ["member", "member", "casual", "casual"],
            "rideable_type": ["electric", "classic", "electric", "classic"],
        },
        index=pd.Index([1, 2, 3, 4]),
    )

    result = lyft_bikes.apply_pricing(
        duration=df["duration"],
        member=df["casual_member"] == "member",
        electric_bike=df["rideable_type"] == "electric",
    )

    assert np.all(result.index == df.index)
    assert isinstance(result, pd.Series)
    assert result.isnull().sum() == 1
