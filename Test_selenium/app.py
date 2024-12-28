from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get ("http://127.0.0.1:8080/")

search_box = driver.find_element(By.ID, "text_box")

search_box.send_keys("Yellowstone")
time.sleep(3)
search_box.send_keys(Keys.CONTROL + "a")  # Select all text (works on Windows/Linux)
search_box.send_keys(Keys.BACKSPACE)  # Delete all selected text
time.sleep(3)

driver.quit()