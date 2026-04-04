import allure
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Корзина")
@allure.story("Оформление заказа")
@allure.title("Проверка оформления заказа с тремя товарами")
@allure.description(
    "Тест проверяет процесс оформления заказа: "
    "авторизация, добавление трех товаров в корзину, "
    "заполнение формы и проверка итоговой суммы"
)
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открытие страницы авторизации"):
            login_page.open()

        with allure.step("Ввод логина standard_user"):
            login_page.enter_username("standard_user")

        with allure.step("Ввод пароля secret_sauce"):
            login_page.enter_password("secret_sauce")

        with allure.step("Нажатие кнопки Login"):
            login_page.click_login()

        with allure.step("Добавление рюкзака в корзину"):
            inventory_page.add_backpack()

        with allure.step("Добавление футболки в корзину"):
            inventory_page.add_bolt_tshirt()

        with allure.step("Добавление комбинезона в корзину"):
            inventory_page.add_onesie()

        with allure.step("Переход в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Нажатие кнопки Checkout"):
            cart_page.click_checkout()

        with allure.step("Ввод имени Мария"):
            checkout_page.enter_first_name("Мария")

        with allure.step("Ввод фамилии Симонова"):
            checkout_page.enter_last_name("Симонова")

        with allure.step("Ввод почтового индекса 5004145"):
            checkout_page.enter_postal_code("5004145")

        with allure.step("Нажатие кнопки Continue"):
            checkout_page.click_continue()

        with allure.step("Получение итоговой суммы"):
            total = checkout_page.get_total()

        with allure.step("Проверка итоговой суммы"):
            assert total == "Total: $58.29", (
                f"Ожидалось 'Total: $58.29', получено '{total}'"
            )

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()


if __name__ == "__main__":
    test_saucedemo()
