import requests
import uuid

def test_create_project_positive(base_url, headers):
    """Позитивный тест: создание проекта"""
    project_name = f"Проект {uuid.uuid4().hex[:4]}"

    response = requests.post(
        f"{base_url}/projects",
        json={"title": project_name},
        headers=headers,
    )

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative(base_url):
    """Негативный тест: создание проекта без авторизации"""
    project_name = f"Проект {uuid.uuid4().hex[:4]}"

    response = requests.post(
        f"{base_url}/projects",
        json={"title": project_name},
        # headers
    )

    assert response.status_code == 401