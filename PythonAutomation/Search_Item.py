import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

url="http://www.tutorialsninja.com/demo/"
expected_product_title='iPhone'
with open('../xpath.json','r') as my_input:
    xpath_input= json.load(my_input)

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get(url)
driver.maximize_window()

driver.find_element_by_xpath(xpath_input['HomePage']['search_field']).send_keys('iphone')
driver.find_element_by_xpath(xpath_input['HomePage']['search_btn']).click()
# print(driver.find_element_by_xpath(search_caption).text)
assert driver.find_element_by_xpath(xpath_input['HomePage']['search_caption']).text == 'iPhone', 'FAIL'
driver.find_element_by_xpath(xpath_input['HomePage']['search_caption']).click()
actual_product_title =driver.find_element_by_xpath(xpath_input['HomePage']['product_title']).text

assert actual_product_title == expected_product_title
driver.find_element_by_xpath(xpath_input['HomePage']['Add_t_Cart_btn']).click()
time.sleep(3)
my_cart_value = driver.find_element_by_xpath(xpath_input['HomePage']['cart']).text
assert '2 item(s)' in my_cart_value
driver.close()