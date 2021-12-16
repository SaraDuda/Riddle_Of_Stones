#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")

# Finding the elements - Riddle of Stone

input_ros1 = browser.find_element(By.CSS_SELECTOR, "input[id='r1Input']")
button_ros1 = browser.find_element(By.CSS_SELECTOR, "button[id='r1Btn']")
answer_ros1 = browser.find_element(By.XPATH, "//div[@id='passwordBanner']/h4").get_attribute("innerText")

# Finding the elements - Riddle of Secrets

input_ros2 = browser.find_element(By.CSS_SELECTOR, "input[id='r2Input']")
button_ros2 = browser.find_element(By.CSS_SELECTOR, "button[id='r2Butn']")

# Finding elements - the Two Merchants

merchant1_value = browser.find_element(By.XPATH, "//b[text()='Jessica']/../../p").get_attribute("innerHTML")
merchant2_value = browser.find_element(By.XPATH, "//b[text()='Bernard']/../../p").get_attribute("innerHTML")
merchant1_name = browser.find_element(By.XPATH, "//b[text()='Jessica']").get_attribute("innerText")
merchant2_name = browser.find_element(By.XPATH, "//b[text()='Bernard']").get_attribute("innerText")

input_max_merchants = browser.find_element(By.CSS_SELECTOR, "input[id='r3Input']")
button_max_merchants = browser.find_element(By.CSS_SELECTOR, "button[id='r3Butn']")

# Finding elements -Answers

button_check_answers = browser.find_element(By.CSS_SELECTOR, "button[id='checkButn']")

final_message = browser.find_element(By.XPATH, "//div[@id='trialCompleteBanner']/h4").get_attribute("innerText")

# Finding max and assigning a name of the wealthiest merchant

if merchant1_value > merchant2_value:
    maximum_value = merchant1_name
else:
    maximum_value = merchant2_name

# Manipulating elements

input_ros1.send_keys("rock")
button_ros1.click()
input_ros2.send_keys(answer_ros1)
button_ros2.click()
input_max_merchants.send_keys(maximum_value)
button_max_merchants.click()
button_check_answers.click()


# Test

class Test(unittest.TestCase):
    def tearDown(self):
        browser.quit()

    def test(self):
        testcase = final_message
        expected = "Trial Complete"
        self.assertEqual(testcase, expected)


unittest.main()
