from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины"""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self) -> None:
        """
        Нажатие на кнопку оформления заказа (Checkout)

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-test='checkout']")
            )
        )
        button.click()
