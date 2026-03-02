import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo():
    driver = webdriver.Firefox()
    
    try:
      
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-list']"))
        )
        
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']").click()
        
        driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
        
        driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        
        driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("мария")
        driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("симонова")
        driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("5004145")
        
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))
        )
        total_text = total_element.text
        
        assert total_text == "Total: $58.29", f"Ожидалось 'Total: $58.29', получено '{total_text}'"
        
        print(f"\n Тест пройден! Итоговая сумма: {total_text}")
        
    finally:
        driver.quit()