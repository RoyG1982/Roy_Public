from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get ("http://127.0.0.1:8080/")

l_username = driver.find_element(By.ID, "l_username")
l_password = driver.find_element(By.ID, "l_password")
login_button = driver.find_element(By.ID, "login_button")

l_username.send_keys("roy")
l_password.send_keys("123")
login_button.click()

time.sleep(60)