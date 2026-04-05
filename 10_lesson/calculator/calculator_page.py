from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей калькулятора"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открытие страницы калькулятора

        :return: None
        """
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, seconds: str) -> None:
        """
        Установка задержки перед вычислением

        :param seconds: str - количество секунд задержки
        :return: None
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_number(self, num: str) -> None:
        """
        Нажатие на кнопку с цифрой

        :param num: str - цифра для нажатия (например, "1", "2", "3")
        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{num}']")
            )
        )
        button.click()

    def click_plus(self) -> None:
        """
        Нажатие на кнопку сложения (+)

        :return: None
        """
        plus = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='+']")
            )
        )
        plus.click()

    def click_equals(self) -> None:
        """
        Нажатие на кнопку равно (=)

        :return: None
        """
        equals = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='=']")
            )
        )
        equals.click()

    def wait_for_result(self, expected_result: str, timeout: int = 50) -> str:
        """
        Ожидание появления ожидаемого результата на экране

        :param expected_result: str - ожидаемый текст результата
        :param timeout: int - максимальное время ожидания в секундах
        :return: str - текст результата с экрана калькулятора
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_result
            )
        )
        screen = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text
