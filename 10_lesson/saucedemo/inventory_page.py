from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс для работы со страницей товаров"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self) -> None:
        """
        Добавление рюкзака (Sauce Labs Backpack) в корзину

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "[data-test='add-to-cart-sauce-labs-backpack']")
            )
        )
        button.click()

    def add_bolt_tshirt(self) -> None:
        """
        Добавление футболки (Sauce Labs Bolt T-Shirt) в корзину

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
            )
        )
        button.click()

    def add_onesie(self) -> None:
        """
        Добавление комбинезона (Sauce Labs Onesie) в корзину

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "[data-test='add-to-cart-sauce-labs-onesie']")
            )
        )
        button.click()

    def go_to_cart(self) -> None:
        """
        Переход в корзину

        :return: None
        """
        link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "[data-test='shopping-cart-link']")
            )
        )
        link.click()
