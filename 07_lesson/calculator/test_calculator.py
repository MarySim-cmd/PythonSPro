from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        page = CalculatorPage(driver)
        
        page.open()
        page.set_delay("45")
        page.click_number("7")
        page.click_plus()
        page.click_number("8")
        page.click_equals()
        
        result = page.wait_for_result("15")
        
        assert result == "15"
        
    finally:
        driver.quit()