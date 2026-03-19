# test_get.py
import pytest
import requests
import uuid

# настройки
BASE_URL = "https://yougile.com/api-v2"
TOKEN = "0011010"  # реальный токен

def create_test_project():
    """создает тестовый проект и возвращает его ID"""
    project_name = f"Проект {uuid.uuid4().hex[:4]}"
    response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": project_name},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    return response.json()["id"]

def test_get_project_positive():
    """позитивный тест: получение проекта по ID (GET)"""
    # создаем проект
    project_id = create_test_project()
    
    # получаем проект по ID
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    
    # проверка
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_get_project_negative():
    """негативный тест: получение несуществующего проекта (GET)"""
    # несуществующий ID
    fake_id = "00000000-0000-0000-0000-000000000000"
    
    response = requests.get(
        f"{BASE_URL}/projects/{fake_id}",
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    
    # проверка
    assert response.status_code == 404