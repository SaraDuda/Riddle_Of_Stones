#!/usr/bin/env python3

from selenium import webdriver
from Page_Object import ROSPage

# Test setup
browser = webdriver.Chrome()
riddles_page = ROSPage(driver=browser)
riddles_page.go()

# Test Riddle Of Stones
riddles_page.stones_input.find()
riddles_page.stones_input.write("rock")
riddles_page.stones_button.find()
assert riddles_page.stones_button.text == "Answer", "Not correct button for Riddle Of Stones"
riddles_page.stones_button.click()
riddles_page.stones_answer.find()
assert riddles_page.stones_answer.text == "bamboo", "Wrong answer for Riddle Of Stones"

# Test Riddle of Secrets
riddles_page.secrets_input.find()
riddles_page.secrets_input.write(riddles_page.stones_answer.text)
riddles_page.secrets_button.find()
assert riddles_page.secrets_button.text == "Answer", "Not correct button for Riddle Of Secrets"
riddles_page.secrets_button.click()
riddles_page.secrets_answer.find()
assert riddles_page.secrets_answer.text == "Success!", "Wrong answer for Riddle Of Secrets"

# Comparing merchants
if riddles_page.merchant_1_value.text > riddles_page.merchant_2_value.text:
    wealthier_merchant = riddles_page.merchant_1_name.text
else:
    wealthier_merchant = riddles_page.merchant_2_name.text

# Test Merchants
riddles_page.merchants_input.find()
riddles_page.merchant_1_name.find()
riddles_page.merchants_input.write(wealthier_merchant)
riddles_page.merchants_button.find()
assert riddles_page.merchants_button.text == 'Answer', "Not correct button for The Two Merchants"
riddles_page.merchants_button.click()
riddles_page.merchants_answer.find()
assert riddles_page.merchants_answer.text == "Success!", "Wrong answer for The Two Merchants"

# Test of Final message
riddles_page.final_button.find()
assert riddles_page.final_button.text == "Check Answers", "Not correct button for final check"
riddles_page.final_button.click()
riddles_page.final_answer.find()
assert riddles_page.final_answer.text == "Trial Complete", "You failed"

print("Everything went well, congrats!")

browser.quit()
