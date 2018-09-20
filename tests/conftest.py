"""Test fixtures"""

import os

import pytest


@pytest.fixture()
def coutwildrnp_geojsons_path():
    return os.path.join(os.path.dirname(__file__), "data/coutwildrnp.geojsons")
