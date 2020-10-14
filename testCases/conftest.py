from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\test\\chromedriver.exe")
    elif browser =='firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\Admin\\Desktop\\test\\geckodriver.exe")
    else:
        driver = webdriver.safari()
    return driver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\test\\chromedriver.exe")
    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\Admin\\Desktop\\test\\geckodriver.exe")
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):  # This will get the value from Command Line (CLI)
    parser.addoption("--browser")

@pytest.fixture(scope='class')
def browser(request):  # This will return the Browser value to setUp method
    return request.config.getoption("--browser")


# PyTest HTML Report adding extra details
def pytest_configure(config):
    config._metadata['Project'] = 'eCommernce bluestone'
    config._metadata['Tester'] = 'PracticeWithArjya'

# To remove some details in HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
