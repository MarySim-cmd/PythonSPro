# test_put.py
import pytest
import requests
import uuid

# Настройки
BASE_URL = "https://yougile.com/api-v2"
TOKEN = "0011010"  # реальный токен

def create_test_project():
    """Создает тестовый проект и возвращает его ID"""
    project_name = f"Проект {uuid.uuid4().hex[:4]}"
    response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": project_name},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    return response.json()["id"]

def test_update_project_positive():
    """Позитивный тест: изменение названия проекта (PUT)"""
    # Создаем проект
    project_id = create_test_project()
    
    # Меняем название
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": "Новое название"},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    
    # Проверка
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_update_project_negative():
    """Негативный тест: изменение несуществующего проекта (PUT)"""
    # Несуществующий ID
    fake_id = "00000000-0000-0000-0000-000000000000"
    
    response = requests.put(
        f"{BASE_URL}/projects/{fake_id}",
        json={"title": "Новое название"},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    
    # Проверка
    assert response.status_code == 404