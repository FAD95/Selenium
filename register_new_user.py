import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from dotenv import load_dotenv
import os

load_dotenv()

class RegisterNewUser(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
    
    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, "/html/body/div/div[2]/header/div/div[2]/div/a/span[2]").click()
        driver.find_element(By.LINK_TEXT, "Log In").click()
        create_account_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a")

        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual("Create New Customer Account", driver.title)

        first_name = driver.find_element(By.ID, "firstname")
        middle_name = driver.find_element(By.ID, "middlename")
        last_name = driver.find_element(By.ID, "lastname")
        email = driver.find_element(By.ID, "email_address")
        password = driver.find_element(By.ID, "password")
        confirm_password = driver.find_element(By.ID, "confirmation")
        newsletter = driver.find_element(By.ID, "is_subscribed")
        submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button")


        self.assertTrue(first_name.is_enabled()
                        and last_name.is_enabled()
                        and email.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and newsletter.is_enabled()
                        and submit_button.is_enabled())
        
        first_name.send_keys(os.getenv("FIRST_NAME"))
        middle_name.send_keys(os.getenv("MIDDLE_NAME"))
        last_name.send_keys(os.getenv("LAST_NAME"))
        email.send_keys(os.getenv("EMAIL"))
        PASSWORD = os.getenv("PASSWORD")
        password.send_keys(PASSWORD)
        confirm_password.send_keys(PASSWORD)
        newsletter.click()
        submit_button.click()


    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'find-elements-report'))

