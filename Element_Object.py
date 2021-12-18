#!/usr/bin/env python3

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(mark=self.locator))
        element.click()
        return None

    def write(self, command):
        element = self.web_element
        element.send_keys(command)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text
