import pytest
import requests
import uuid


@pytest.fixture(scope="session")
def base_url():
    return "https://yougile.com/api-v2"


@pytest.fixture(scope="session")
def token():
    return "токен-тут"


@pytest.fixture(scope="session")
def headers(token):
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def created_project(base_url, headers):
    """Создаёт проект перед тестом и возвращает его ID"""
    project_name = f"Проект {uuid.uuid4().hex[:4]}"
    response = requests.post(
        f"{base_url}/projects",
        json={"title": project_name},
        headers=headers,
    )
    return response.json()["id"]