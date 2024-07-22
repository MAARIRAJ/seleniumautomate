from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.youtube.com")
search_bar=driver.find_element(By.NAME,"search_query")
search_bar.send_keys("video song")
time.sleep(2)
search_btn=driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']")
search_btn.click()
time.sleep(5)
video=driver.find_element(By.CSS_SELECTOR,"a#video-title")
video.click()
time.sleep(10)
driver.close()

