import requests

def test_get_project_positive(base_url, headers, created_project):
    """Позитивный тест: получение проекта по ID (GET)"""
    response = requests.get(
        f"{base_url}/projects/{created_project}",
        headers=headers,
    )

    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_get_project_negative(base_url, headers):
    """Негативный тест: получение несуществующего проекта (GET)"""
    fake_id = "00000000-0000-0000-0000-000000000000"

    response = requests.get(
        f"{base_url}/projects/{fake_id}",
        headers=headers,
    )

    assert response.status_code == 404