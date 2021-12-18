#!/usr/bin/env

from selenium.webdriver.common.by import By
from Element_Object import BaseElement


class ROSPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/trial-of-the-stones"

    def __base_element_locator(self, by, value):
        return BaseElement(driver=self.driver, by=by, value=value)

    def go(self):
        self.driver.get(self.url)

    @property
    def stones_input(self):
        return self.__base_element_locator(By.ID, "r1Input")

    @property
    def stones_button(self):
        return self.__base_element_locator(By.NAME, "r1Btn")

    @property
    def stones_answer(self):
        return self.__base_element_locator(By.CSS_SELECTOR, "div#passwordBanner h4")

    @property
    def secrets_input(self):
        return self.__base_element_locator(By.ID, "r2Input")

    @property
    def secrets_button(self):
        return self.__base_element_locator(By.NAME, "r2Butn")

    @property
    def secrets_answer(self):
        return self.__base_element_locator(By.CSS_SELECTOR, "div#successBanner1 h4")

    @property
    def merchant_1_name(self):
        return self.__base_element_locator(By.XPATH, "//b[text()='Jessica']")

    @property
    def merchant_1_value(self):
        return self.__base_element_locator(By.XPATH, "//b[text()='Jessica']/../../p")

    @property
    def merchant_2_name(self):
        return self.__base_element_locator(By.XPATH, "//b[text()='Bernard']")

    @property
    def merchant_2_value(self):
        return self.__base_element_locator(By.XPATH, "//b[text()='Bernard']/../../p")

    @property
    def merchants_input(self):
        return self.__base_element_locator(By.ID, "r3Input")

    @property
    def merchants_answer(self):
        return self.__base_element_locator(By.CSS_SELECTOR, "div#successBanner2 h4")

    @property
    def merchants_button(self):
        return self.__base_element_locator(By.NAME, "r3Butn")

    @property
    def final_button(self):
        return self.__base_element_locator(By.NAME, "checkButn")

    @property
    def final_answer(self):
        return self.__base_element_locator(By.CSS_SELECTOR, "div#trialCompleteBanner h4")
