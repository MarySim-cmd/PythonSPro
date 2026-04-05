from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для работы со страницей авторизации"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открытие страницы авторизации

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя

        :param username: str - имя пользователя
        :return: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='username']")
            )
        )
        field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввод пароля

        :param password: str - пароль
        :return: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='password']")
            )
        )
        field.send_keys(password)

    def click_login(self) -> None:
        """
        Нажатие на кнопку входа (Login)

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-test='login-button']")
            )
        )
        button.click()
