from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException


def test_cookie1():

    driver.get("http://localhost:1667/#/")

    cookies = driver.find_element_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]")

    print(cookies.is_displayed())
    print(cookies.is_enabled())

    print(driver.get_cookies())

    accept = driver.find_element_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]/button[2]/div")
    accept.click()

    print(driver.get_cookies())

    time.sleep(2)

    driver.get("https://www.python.org/")
    time.sleep(2)
    driver.get("http://localhost:1667/#/")
    time.sleep(2)
    print(driver.get_cookies())
    time.sleep(2)
    driver.close()
    time.sleep(2)

    print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("https://www.google.com/")
    except Exception as e:
        print(e)


test_cookie1()





