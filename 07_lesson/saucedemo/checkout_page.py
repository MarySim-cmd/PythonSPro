from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def enter_first_name(self, first_name):
        field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='firstName']")))
        field.send_keys(first_name)
    
    def enter_last_name(self, last_name):
        field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='lastName']")))
        field.send_keys(last_name)
    
    def enter_postal_code(self, postal_code):
        field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='postalCode']")))
        field.send_keys(postal_code)
    
    def click_continue(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='continue']")))
        button.click()
    
    def get_total(self):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']")))
        return element.text