from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/dynamicid")
    
   #ВАЖНО: НЕ ИСПОЛЬЗОВАТЬ ID (он динамический)
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    
    print("✓ Клик по кнопке выполнен успешно!")

finally:
    driver.quit()