import requests
import pytest


def get_vacancies(text):
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies")
    return response.json()   # Получение вакансий API "Работа России"

def test_vacancies_status_code():
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies")
    assert response.status_code == 200   # Проверка статус (код) ответа 200


def test_vacancies_headers():
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies")
    assert response.headers['Content-Type'] == "application/json;charset=utf-8"  # Проверка формата данных в ответе 


def test_vacancies_schedule():
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies")
    response_body = response.json()
    assert response_body["results"]["vacancies"][0]["vacancy"]["schedule"] == "Полный рабочий день"   # Проверка графика труда первой вакансии
