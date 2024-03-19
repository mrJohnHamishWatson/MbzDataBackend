import requests
from tests.conftest import base_url, prompt_data


def test_get_events_by_user(base_url, prompt_data):
    url = f"{base_url}/search"

    # Define the request body

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Send the POST request
    response = requests.post(url, json=prompt_data, headers=headers)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response body or perform other validations as needed
    response_data = response.json()
    print(response_data)

