


#File Name should start with test_ or end with _test
#pip install pytest
#pip install pytest-html

#each test should be defined inside a function
#test function should start with test_ or end with _test
import pytest
import json
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

with open('../xpath.json','r') as my_input:
    xpath_input= json.load(my_input)

url="http://www.tutorialsninja.com/demo/"
expected_product_title='iPhone'
expected_logout_msg='Account Logout'
driver=None

@pytest.fixture()
def setup():
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
#@pytest.mark.skip
@pytest.mark.xfail
def test_registration(setup):
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
    msg = driver.find_element_by_xpath(xpath_input['Registration']['success_msg']).text
    print(msg)
    assert msg == 'Your Account Has Been Created!'

def test_login(setup):
    driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_id(xpath_input['LoginPage']['email_input_id']).send_keys('testid@gmail.com')
    driver.find_element_by_id(xpath_input['LoginPage']['password_input_id']).send_keys('Test@123')
    driver.find_element_by_xpath(xpath_input['LoginPage']['login_btn']).click()
    actual_text = driver.find_element_by_xpath(xpath_input['LoginPage']['expected_login_page']).text
    assert actual_text == 'My Account'

@pytest.mark.usefixtures('setup')
def test_add_t_cart():
    driver.find_element_by_xpath(xpath_input['HomePage']['search_field']).send_keys('iphone')
    driver.find_element_by_xpath(xpath_input['HomePage']['search_btn']).click()
    # print(driver.find_element_by_xpath(search_caption).text)
    assert driver.find_element_by_xpath(xpath_input['HomePage']['search_caption']).text == 'iPhone', 'FAIL'
    driver.find_element_by_xpath(xpath_input['HomePage']['search_caption']).click()
    actual_product_title = driver.find_element_by_xpath(xpath_input['HomePage']['product_title']).text
    assert actual_product_title == expected_product_title
    driver.find_element_by_xpath(xpath_input['HomePage']['Add_t_Cart_btn']).click()
    time.sleep(3)
    my_cart_value = driver.find_element_by_xpath(xpath_input['HomePage']['cart']).text
    assert '1 item(s)' in my_cart_value

def test_logout(setup):
    driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
    time.sleep(3)
    driver.find_element_by_link_text('Logout').click()
    time.sleep(3)
    actual_logout_msg = driver.find_element_by_xpath(xpath_input['Logout']['logout_msg']).text
    assert expected_logout_msg == actual_logout_msg
    driver.close()

