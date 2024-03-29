#!/usr/loacl/bin/python3
# -*- coding: UTF-8 -*-
# Filename: ifram_01.py
# __Author__: zhaoyunhe
# data: 2019/8/1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://mail.126.com/")
        driver.find_element_by_id("switchAccountLogin").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=3 | ]]
        driver.find_element_by_id("auto-id-1564654265837").click()
        driver.find_element_by_id("auto-id-1564654265837").clear()
        driver.find_element_by_id("auto-id-1564654265837").send_keys("mhj6868")
        driver.find_element_by_id("auto-id-1564654265840").clear()
        driver.find_element_by_id("auto-id-1564654265840").send_keys("131417")
        driver.find_element_by_id("dologin").click()
        driver.find_element_by_id("auto-id-1564654265840").click()
        driver.find_element_by_id("auto-id-1564654265840").clear()
        driver.find_element_by_id("auto-id-1564654265840").send_keys("131417zou")
        driver.find_element_by_id("dologin").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
