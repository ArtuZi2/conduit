from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
"""
options.add_argument('--headless')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("http://localhost:1667")"""
import pytest


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:1667/#/")
    return driver


def test_login(browser):
    time.sleep(2)
    navbar = browser.find_elements_by_class_name("ion-compose")
    #át lehet ezt alakítani, hogy kiírja a navban elemeit?
    print(navbar)

    time.sleep(2)

    element = browser.find_element_by_xpath("//a[@href='#/register']")
    print(element.is_enabled())
    print(element.is_displayed())

    emil = "tkata@gmail.com"
    password = "Sunshine2046"

    element.click()
    time.sleep(2)
    browser.find_element_by_xpath("//fieldset[1]/input").send_keys(emil)
    time.sleep(2)
    browser.find_element_by_xpath("//fieldset[2]/input").send_keys(password)
    time.sleep(2)
    browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a").click()
    time.sleep(2)
    user_setting = browser.find_element_by_tag_name("h4")
    time.sleep(2)
    print(user_setting.text)
    user = "sun2"

    assert user == user_setting.text

    #driver.find_element_by_xpath("//a [@active-class='active']").click()


#driver.close()
