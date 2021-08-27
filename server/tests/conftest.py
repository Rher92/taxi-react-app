import os

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

SU_USERNAME = "superuser"
SU_EMAIL = "superuser@email.com"
SU_PASSWORD = "superuser"

USERNAME = "username"
EMAIL = "user@email.com"
PASSWORD = "user1234"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get(
            "POSTGRES_DB", os.path.join(settings.BASE_DIR, "db.sqlite3")
        ),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }


@pytest.fixture(scope="session")
def superuser():
    def _create_super_user():
        UserClass = get_user_model()
        su = UserClass.objects.create_user(
            username=SU_USERNAME,
            email=SU_EMAIL,
            password=SU_PASSWORD,
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        return su

    return _create_super_user


@pytest.fixture(scope="session")
def user():
    def _create_user():
        UserClass = get_user_model()
        user = UserClass.objects.create_user(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD,
            is_staff=False,
            is_active=True,
            is_superuser=False,
        )
        return user

    return _create_user


@pytest.fixture(scope="module")
def get_access_token():
    def _login(user, client):
        client.force_login(user)
        if user.username == "superuser":
            password = SU_PASSWORD
        endpoint = reverse("token_obtain_pair")
        data = {"username": user.username, "password": password}
        content_type = "application/json"

        get_token = client.post(
            endpoint,
            data=data,
            content_type=content_type,
        )

        return get_token.data["access"]

    return _login
