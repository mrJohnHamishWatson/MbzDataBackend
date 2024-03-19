import pytest


@pytest.fixture()
def prompt_data():
    data = {
            "prompt": "Smells like Teen Spirit",
            }
    return data


@pytest.fixture()
def base_url():
    return "http://127.0.0.1:5111"
