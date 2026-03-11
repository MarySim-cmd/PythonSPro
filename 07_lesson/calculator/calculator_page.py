from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)
    
    def click_number(self, num):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{num}']"))
        )
        button.click()
    
    def click_plus(self):
        plus = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        )
        plus.click()
    
    def click_equals(self):
        equals = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        )
        equals.click()
    
    def wait_for_result(self, expected_result, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result)
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text