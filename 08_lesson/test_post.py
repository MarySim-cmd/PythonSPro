# test_post.py
import pytest
import requests
import uuid

# Настройки
BASE_URL = "https://yougile.com/api-v2"
TOKEN = "0011010"  # токен

def test_create_project_positive():
    """Позитивный тест: создание проекта"""
    # Подготовка данных
    project_name = f"Проект {uuid.uuid4().hex[:4]}"
    
    # Запрос
    response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": project_name},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    
    # Проверки
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative():
    """Негативный тест: создание проекта без авторизации"""
    # Подготовка данных
    project_name = f"Проект {uuid.uuid4().hex[:4]}"
    
    # Запрос без токена
    response = requests.post(
        f"{BASE_URL}/projects",
        json={"title": project_name}
    )
    
    # Проверка
    assert response.status_code == 401