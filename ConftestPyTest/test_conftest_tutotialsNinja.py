#File Name should start with test_ or end with _test
#pip install pytest
#pip install pytest-html

#each test should be defined inside a function
#File Name should start with test_ or end with _test
#pip install pytest
#pip install pytest-html

#each test should be defined inside a function
#test function should start with test_ or end with _test
#ClassName should start with Test
import pytest
import json
import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

with open('../xpath.json','r') as my_input:
    xpath_input= json.load(my_input)

url="http://www.tutorialsninja.com/demo/"
expected_product_title='iPhone'
expected_logout_msg='Account Logout'
#driver=None

@pytest.mark.usefixtures('setup')
class Test_E2E:
    @pytest.mark.skip
    def test_registration(self):
        self.driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
        self.driver.find_element_by_link_text('Register').click()
        self.driver.find_element_by_id(xpath_input['Registration']['first_name_id']).send_keys('tutorials')
        self.driver.find_element_by_id(xpath_input['Registration']['last_name_id']).send_keys('ninja')
        self.driver.find_element_by_id(xpath_input['Registration']['email_id']).send_keys('testid@gmail.com')
        self.driver.find_element_by_id(xpath_input['Registration']['phone_id']).send_keys('9868123456')
        self.driver.find_element_by_id(xpath_input['Registration']['password_id']).send_keys('Test@123')
        self.driver.find_element_by_id(xpath_input['Registration']['password_confirmation_id']).send_keys('Test@123')
        self.driver.find_element_by_xpath(xpath_input['Registration']['agree_checkbox']).click()
        self.driver.find_element_by_xpath(xpath_input['Registration']['continue_button']).click()
        msg = self.driver.find_element_by_xpath(xpath_input['Registration']['success_msg']).text
        print(msg)
        assert msg == 'Your Account Has Been Created!'
    
    def test_login(self):
        self.driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_id(xpath_input['LoginPage']['email_input_id']).send_keys('testid@gmail.com')
        self.driver.find_element_by_id(xpath_input['LoginPage']['password_input_id']).send_keys('Test@123')
        self.driver.find_element_by_xpath(xpath_input['LoginPage']['login_btn']).click()
        actual_text = self.driver.find_element_by_xpath(xpath_input['LoginPage']['expected_login_page']).text
        assert actual_text == 'My Account'
    
    #@pytest.mark.usefixtures
    def test_add_t_cart(self):
        self.driver.find_element_by_xpath(xpath_input['HomePage']['search_field']).send_keys('iphone')
        self.driver.find_element_by_xpath(xpath_input['HomePage']['search_btn']).click()
        # print(self.driver.find_element_by_xpath(search_caption).text)
        assert self.driver.find_element_by_xpath(xpath_input['HomePage']['search_caption']).text == 'iPhone', 'FAIL'
        self.driver.find_element_by_xpath(xpath_input['HomePage']['search_caption']).click()
        actual_product_title = self.driver.find_element_by_xpath(xpath_input['HomePage']['product_title']).text
        assert actual_product_title == expected_product_title
        self.driver.find_element_by_xpath(xpath_input['HomePage']['Add_t_Cart_btn']).click()
        time.sleep(3)
        my_cart_value = self.driver.find_element_by_xpath(xpath_input['HomePage']['cart']).text
        assert '1 item(s)' in my_cart_value
    
    def test_logout(self):
        self.driver.find_element_by_xpath(xpath_input['Registration']['Account_Button']).click()
        time.sleep(3)
        self.driver.find_element_by_link_text('Logout').click()
        time.sleep(3)
        actual_logout_msg = self.driver.find_element_by_xpath(xpath_input['Logout']['logout_msg']).text
        assert expected_logout_msg == actual_logout_msg
        self.driver.close()

