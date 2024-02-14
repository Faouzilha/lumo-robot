# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_creer_test_case(self):
        driver = self.driver
        driver.get(self.base_url + chrome://newtab/)
        driver.get("https://magento.softwaretestingboard.com/?ref=hackernoon.com")
        driver.find_element(By.LINK_TEXT,"Create an Account").click()
        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        driver.find_element(By.ID,"firstname").click()
        driver.find_element(By.ID,"firstname").clear()
        driver.find_element(By.ID,"firstname").send_keys("Sonny")
        driver.find_element(By.ID,"lastname").click()
        driver.find_element(By.ID,"lastname").clear()
        driver.find_element(By.ID,"lastname").send_keys("Melissa")
        driver.find_element(By.ID,"email_address").click()
        driver.find_element(By.ID,"email_address").clear()
        driver.find_element_by_id("email_address").send_keys("sonny@exemple.com")
        driver.find_element(By.ID,"password").click()
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys("Sonny1306.")
        driver.find_element(By.ID,"password-confirmation").click()
        driver.find_element(By.ID,"password-confirmation").clear()
        driver.find_element(By.ID,"password-confirmation").send_keys("Sonny1306.")
        driver.find_element_by_xpath("//form[@id='form-validate']/div/div/button/span/font/font").click()
        driver.get("https://magento.softwaretestingboard.com/customer/account/")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('Ma liste d', \"'\", 'envies')])[1]/following::font[2]").click()
        driver.get("https://magento.softwaretestingboard.com/")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
