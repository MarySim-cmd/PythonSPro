"""
Модуль с тестами для калькулятора.

Здесь тесты проверки работы калькулятора с установкой задержки.
"""

from selenium import webdriver
from calculator_page import CalculatorPage
import allure


@allure.feature("Калькулятор")
@allure.story("Проверка арифметических операций")
@allure.title("Тест сложения 7 + 8 = 15")
@allure.description(
    "Тест проверяет работу калькулятора с установленной задержкой. "
    "Выполняется сложение 7 + 8, ожидается = 15."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator() -> None:
    """
    Тест сложения двух чисел на калькуляторе с задержкой.

    Шаги теста:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Нажать кнопку 7
    4. Нажать кнопку плюс
    5. Нажать кнопку 8
    6. Нажать кнопку равно
    7. Ожидать результат = 15
    8. Проверить, что результат = 15

    Returns:
        None
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Инициализировать страницу калькулятора"):
            page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay("45")

        with allure.step("Ввести число 7"):
            page.click_number("7")

        with allure.step("Нажать операцию сложения (+)"):
            page.click_plus()

        with allure.step("Ввести число 8"):
            page.click_number("8")

        with allure.step("Нажать кнопку равно (=)"):
            page.click_equals()

        with allure.step("Ожидать результат 15 на экране"):
            result = page.wait_for_result("15")

        with allure.step("Проверить результат сложения"):
            assert result == "15", (
                f"Ожидался результат '15', получен '{result}'"
            )

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()
