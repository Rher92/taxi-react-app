import base64
import json

import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse

PASSWORD = "pAssw0rd!"


@pytest.mark.django_db
def test_user_can_sign_up(client):
    response = client.post(
        reverse("signup-list"),
        data={
            "username": "user@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": PASSWORD,
            "password2": PASSWORD,
        },
    )
    user = get_user_model().objects.last()
    assert status.HTTP_201_CREATED == response.status_code
    assert response.data["id"] == user.id
    assert response.data["username"] == user.username
    assert response.data["first_name"] == user.first_name
    assert response.data["last_name"] == user.last_name


@pytest.mark.django_db
def test_user_can_login(client, user):
    user = user()
    PASSWORD = "user1234"
    response = client.post(
        reverse("log_in"),
        data={
            "username": user.username,
            "password": PASSWORD,
        },
    )

    # Parse payload data from access token.
    access = response.data["access"]
    header, payload, signature = access.split(".")
    decoded_payload = base64.b64decode(f"{payload}==")
    payload_data = json.loads(decoded_payload)

    import pdb

    pdb.set_trace()
    assert status.HTTP_200_OK == response.status_code
    assert response.data["refresh"] is not None
    assert payload_data["id"] == user.id
    assert payload_data["username"] == user.username
    assert payload_data["first_name"] == user.first_name
    assert payload_data["last_name"] == user.last_name
