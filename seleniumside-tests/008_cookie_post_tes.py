from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import random, string
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())


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
    driver.close()

    #elnavigálni, megnézni, megjelenik-e a cookie még egyszer

test_cookie1()


