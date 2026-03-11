from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def add_backpack(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")))
        button.click()
    
    def add_bolt_tshirt(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")))
        button.click()
    
    def add_onesie(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']")))
        button.click()
    
    def go_to_cart(self):
        link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
        link.click()