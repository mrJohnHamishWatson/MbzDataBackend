import pytest


@pytest.fixture()
def prompt_data():
    data = {
            "prompt": "Король",
            }
    return data


@pytest.fixture()
def base_url():
    return "http://127.0.0.1:5111"
