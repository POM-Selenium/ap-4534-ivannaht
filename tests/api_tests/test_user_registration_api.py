import random

import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/user/register/"


@pytest.fixture
def valid_user_data():
    rn = random.randint(1000, 9999)
    return {
        "first_name": f"Selenium{rn}",
        "last_name": f"Driver{rn}",
        "middle_name": f"Web{rn}",
        "email": f"swd{rn}@test.com",
        "password": f"pass#{rn}",
        "role": "0",
        "is_active": True,
        "is_staff": False
    }


@pytest.mark.parametrize("missing_field", [
    "email",
    "password",
    "role"
])
def test_registration_missing_required_field(valid_user_data, missing_field):
    data = valid_user_data.copy()
    data.pop(missing_field)

    response = requests.post(BASE_URL, json=data)

    assert response.status_code == 400
    assert missing_field in response.json()


def test_register_user_success(valid_user_data):
    response = requests.post(BASE_URL, json=valid_user_data)

    assert response.status_code == 201
    json_data = response.json()

    assert json_data["email"] == valid_user_data["email"]
    assert json_data["first_name"] == valid_user_data["first_name"]
    assert json_data["last_name"] == valid_user_data["last_name"]
    assert "id" in json_data


def test_register_user_duplicate_email(valid_user_data):
    requests.post(BASE_URL, json=valid_user_data)
    response = requests.post(BASE_URL, json=valid_user_data)

    assert response.status_code == 400
    assert "email" in response.json()


def test_register_user_invalid_email(valid_user_data):
    data = valid_user_data.copy()
    data["email"] = "not-an-email"

    response = requests.post(BASE_URL, json=data)

    assert response.status_code == 400
    assert "email" in response.json()


def test_register_user_short_password(valid_user_data):
    data = valid_user_data.copy()
    data["password"] = "123"

    response = requests.post(BASE_URL, json=data)

    assert response.status_code == 400 or response.status_code == 422
