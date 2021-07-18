from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import random, string
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_cookie():

    driver.get("http://localhost:1667/#/")

    cookie = driver.find_element_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]")

    print(cookie.is_displayed())
    print(cookie.is_enabled())

    buttons = driver.find_elements_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]/button"[1])
    buttons_text = "I decline!"
    print(buttons)
    print(buttons_text)


test_cookie()

