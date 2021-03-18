#pip install selenium
#pip install webdriver_manager
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url="http://www.tutorialsninja.com/demo/"

with open('../xpath.json','r') as my_input:
    xpath_input= json.load(my_input)

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
driver.find_element_by_link_text('Register').click()

driver.find_element_by_id(xpath_input['Registration']['first_name_id']).send_keys('tutorials')
driver.find_element_by_id(xpath_input['Registration']['last_name_id']).send_keys('ninja')
driver.find_element_by_id(xpath_input['Registration']['email_id']).send_keys('testid@gmail.com')
driver.find_element_by_id(xpath_input['Registration']['phone_id']).send_keys('9868123456')
driver.find_element_by_id(xpath_input['Registration']['password_id']).send_keys('Test@123')
driver.find_element_by_id(xpath_input['Registration']['password_confirmation_id']).send_keys('Test@123')
driver.find_element_by_xpath(xpath_input['Registration']['agree_checkbox']).click()
driver.find_element_by_xpath(xpath_input['Registration']['continue_button']).click()

msg=driver.find_element_by_xpath(xpath_input['Registration']['success_msg']).text
print(msg)
assert msg=='Your Account Has Been Created!'
driver.close()


