import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url="http://www.tutorialsninja.com/demo/"

with open('../xpath.json','r') as my_input:
    xpath_input= json.load(my_input)

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
driver.find_element_by_link_text('Login').click()
driver.find_element_by_id(xpath_input['LoginPage']['email_input_id']).send_keys('testid@gmail.com')
driver.find_element_by_id(xpath_input['LoginPage']['password_input_id']).send_keys('Test@123')
driver.find_element_by_xpath(xpath_input['LoginPage']['login_btn']).click()
actual_text=driver.find_element_by_xpath(xpath_input['LoginPage']['expected_login_page']).text
assert actual_text=='My Account'
driver.close()

