from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080/")

# home
l_username = driver.find_element(By.ID, "l_username")
l_password = driver.find_element(By.ID, "l_password")
login_button = driver.find_element(By.ID, "login_button")

l_username.send_keys("roy")
l_password.send_keys("123")
login_button.click()

time.sleep(3)

# user_homepage

file_input = driver.find_element(By.ID, "add_txt_file")
file_path = r"C:\Users\User\Desktop\DevOps\Domain_monitoring7\domain_list_5.txt"
file_input.send_keys(file_path)

time.sleep(60)
driver.quit()
