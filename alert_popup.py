import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class CompareProducts(unittest.TestCase):
    """Accept or dismiss alert pop-ups

    Args:
        unittest (): The class that contains the test methods
    """

    @classmethod
    def setUpClass(cls):
        chrome = Service(r"/usr/bin/chromedriver")
        cls.driver = webdriver.Chrome(service=chrome)
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_compare_products_removal_alert(self):
        """Accept or dismiss alert pop-ups"""
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        # como buena práctica se recomienda limpiar los campos
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        # creamos una variable para interactuar con el pop-up
        alert = driver.switch_to.alert
        # vamos a extraer el texto que muestra
        alert_text = alert.text

        # vamos a verificar el texto de la alerta
        self.assertEqual(
            'Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(3)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='find-elements-report'))
