import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_data_types_form_submission_edge():
    driver = None
    try:
        driver = webdriver.Edge()
        driver.maximize_window()

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in form_data.items():
            driver.find_element(By.NAME, field_name).send_keys(value)

        driver.find_element(By.NAME, "zip-code").clear()

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success"))
        )

        assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

        for field_id in form_data.keys():
            assert "success" in driver.find_element(By.ID, field_id).get_attribute("class")

    finally:
        if driver:
            driver.quit()