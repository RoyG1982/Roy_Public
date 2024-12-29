from locust import HttpUser, task, between
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumUser(HttpUser):
    wait_time = between(1, 5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = None

    def on_start(self):
        self.driver = webdriver.Chrome()

    def on_stop(self):
        if self.driver:
            self.driver.quit()

    @task
    def go_to_user_homepage(self):
        self.driver.get("http://127.0.0.1:8080/")

        l_username = self.driver.find_element(By.ID, "l_username")
        l_password = self.driver.find_element(By.ID, "l_password")
        login_button = self.driver.find_element(By.ID, "login_button")

        l_username.send_keys("roy")
        l_password.send_keys("123")
        login_button.click()

        # Wait until the user_homepage page is fully loaded after login
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8080/user_homepage")
        )

        self.client.get("/user_homepage")