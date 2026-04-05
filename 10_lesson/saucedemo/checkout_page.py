from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для работы со страницей оформления заказа"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name: str) -> None:
        """
        Ввод имени

        :param first_name: str - имя
        :return: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='firstName']")
            )
        )
        field.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Ввод фамилии

        :param last_name: str - фамилия
        :return: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='lastName']")
            )
        )
        field.send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """
        Ввод почтового индекса

        :param postal_code: str - почтовый индекс
        :return: None
        """
        field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='postalCode']")
            )
        )
        field.send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажатие на кнопку продолжения (Continue)

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-test='continue']")
            )
        )
        button.click()

    def get_total(self) -> str:
        """
        Получение итоговой суммы заказа

        :return: str - текст с итоговой суммой (например, "Total: $58.29")
        """
        element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-test='total-label']")
            )
        )
        return element.text
