from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    
    driver.get("http://the-internet.herokuapp.com/login")
    
    # username
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    
    # password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # кн Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # текст с зеленой плашки
    text = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
    print("Выполнено успешно")

finally:
    driver.quit()