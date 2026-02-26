from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class wait_for_images_count:
    def __init__(self, count):
        self.count = count
    
    def __call__(self, driver):
        images = driver.find_elements(By.TAG_NAME, "img")
        if len(images) >= self.count:
            all_have_src = all(img.get_attribute("src") for img in images)
            return all_have_src
        return False

driver = webdriver.Chrome()

try:
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    
    WebDriverWait(driver, 15).until(
        wait_for_images_count(4)
    )
    
    images = driver.find_elements(By.TAG_NAME, "img")
    
    print(f"Всего картинок на странице: {len(images)}")
    print("-" * 50)
    
    for i, img in enumerate(images):
        src = img.get_attribute("src")
        print(f"Картинка {i+1}: {src}")
    
    print("-" * 50)
    fourth_image_src = images[3].get_attribute("src")
    print(f"src 3-й картинки (нужная): {fourth_image_src}")
        
finally:
    driver.quit()