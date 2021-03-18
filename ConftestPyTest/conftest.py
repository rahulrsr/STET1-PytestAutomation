import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url="http://www.tutorialsninja.com/demo/"

@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver=driver
    yield
    driver.close()