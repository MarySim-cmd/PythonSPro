from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo():
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        
        inventory_page.add_backpack()
        inventory_page.add_bolt_tshirt()
        inventory_page.add_onesie()
        inventory_page.go_to_cart()
        
        cart_page.click_checkout()
        
        checkout_page.enter_first_name("Мария")
        checkout_page.enter_last_name("Симонова")
        checkout_page.enter_postal_code("5004145")
        checkout_page.click_continue()
        
        total = checkout_page.get_total()
        
        assert total == "Total: $58.29", f"Ожидалось 'Total: $58.29', получено '{total}'"
        
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_saucedemo()