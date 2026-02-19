from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    print("✓ Страница загружена")
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )

    #  Ввести "Sky"
    input_field.send_keys("Sky")
    print("✓ Введен текст: Sky")

    input_field.clear()
    print("✓ Поле очищено")

    # Ввести "Pro"
    input_field.send_keys("Pro")
    print("✓ Введен текст: Pro")

    import time
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
    print("✓ Браузер закрыт, все готово")