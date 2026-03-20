# test_put.py
import requests

def test_update_project_positive(base_url, headers, created_project):
    """Позитивный тест: изменение названия проекта (PUT)"""
    response = requests.put(
        f"{base_url}/projects/{created_project}",
        json={"title": "Новое название"},
        headers=headers,
    )

    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_update_project_negative(base_url, headers):
    """Негативный тест: изменение несуществующего проекта (PUT)"""
    fake_id = "00000000-0000-0000-0000-000000000000"

    response = requests.put(
        f"{base_url}/projects/{fake_id}",
        json={"title": "Новое название"},
        headers=headers,
    )

    assert response.status_code == 404