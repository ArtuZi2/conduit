from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import pytest_order
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


@pytest.mark.order(1)
def test_login():
    emil = "tkata@gmail.com"
    password = "Sunshine2046"

    driver.get("http://localhost:1667/#/")
    time.sleep(2)
    navbar = driver.find_elements_by_class_name("ion-compose")
    #át lehet ezt alakítani, hogy kiírja a navban elemeit?
    print(navbar)

    time.sleep(2)

    element = driver.find_element_by_xpath("//a[@href='#/login']")
    print(element.is_enabled())
    print(element.is_displayed())

    element.click()
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[1]/input").send_keys(emil)
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a").click()

    print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)


test_login()


@pytest.mark.order(2)
def test_logout():

    logout = driver.find_element_by_xpath("//a [@active-class='active']")
    print(logout.is_enabled())
    print(logout.is_displayed())
    logout.click()
    time.sleep(2)
    while True:
        try:
            logout.is_enabled()
            print("Látható")
        except:
            print("Nem látható az oldalon")
            break

    print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)


test_logout()
