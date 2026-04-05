# Проект автоматизации тестирования

## Описание

Проект содержит автотесты для:
- Интернет-магазина Saucedemo (https://www.saucedemo.com/)
- Калькулятора (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)

## Структура проекта
── cart_page.py # Страница корзины (Saucedemo)
── checkout_page.py # Страница оформления заказа (Saucedemo)
── inventory_page.py # Страница товаров (Saucedemo)
── login_page.py # Страница авторизации (Saucedemo)
── calculator_page.py # Страница калькулятора
── test_saucedemo.py # Тесты для интернет-магазина
── test_calculator.py # Тесты для калькулятора
── allure_results/ # Папка с результатами (не пушится)
── README.md # Документация


## Установка и настройка
Установить Firefox с официального сайта

### 1. Установка зависимостей

```bash
pip install selenium pytest allure-pytest

Запуск тестов

Обычный запуск всех тестов:   pytest -v
Запуск конкретного теста:     pytest test_saucedemo.py -v   \\\   pytest test_calculator.py -v


Формирование и просмотр отчета Allure
1. Запуск тестов с формированием результатов:  pytest --alluredir=allure_results
                     macOS:                    brew install allure
      Linux: sudo apt-add-repository ppa:      qameta/allure \\\ sudo apt-get update \\\ sudo apt-get install allure
     Windows: Скачать с официального сайта:    https://github.com/allure-framework/allure2/releases \\\ pip install allure-pytest

Добавить путь к bin в переменную окружения PATH.

3. Просмотр отчета:          allure serve allure_results
После выполнения команды откроется браузер с Allure отчетом.

4. Генерация  отчета:        allure generate allure_results -o allure-report
Открыть отчет в браузере:    allure open allure-report
Очистка результатов:         rm -rf allure_results/   \\\   rm -rf allure-report/

Примечания:
Папки allure_results/ и allure-report/ добавлены в .gitignore
Тесты используют Firefox в качестве браузера по умолчанию

#### Быстрые команды
pytest -v                           Запустить все тесты 
pytest --alluredir=allure_results   Запустить тесты с сохранением результатов 
allure serve allure_results         Сформировать и открыть отчет
rm -rf allure_results/              Очистить результаты 