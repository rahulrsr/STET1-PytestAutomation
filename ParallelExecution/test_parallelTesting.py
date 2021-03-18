#pip install pytest-xdist

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver=None
@pytest.fixture(params=['chrome','ff'],scope='module')
def setup(request):
    global driver
    if request.param=="chrome":
        driver=webdriver.Chrome(ChromeDriverManager().install())
    if request.param=="ff":
        driver=webdriver.Firefox(GeckoDriverManager().install())
    driver.get('http://www.rediff.com')
    driver.maximize_window()
    yield
    driver.close()

def test_first(setup):
    assert driver.current_url=='https://www.rediff.com/'