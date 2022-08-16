from pathlib import Path
from typing import Dict

import json

import pytest


@pytest.fixture
def test_data_dir() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def mock_requests_base(test_data_dir):
    class RequestBaseMock:
        def data(self, url: str) -> Dict:
            file = test_data_dir / self.file_name
            with open(file, "r") as f:
                data = json.load(f)

            return data

    return RequestBaseMock()
