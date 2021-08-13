from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random, string
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException


def test_register():
    username = "sun2"
    password = "Sunshine2046"

    driver.get("http://localhost:1667")
    time.sleep(2)

    def generate_email(prefix='tkata+', domain='gmail.com'):
        random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                              for _ in range(10))

        return prefix + random_part + '@' + domain

    generate_email()

    driver.find_element_by_xpath("/html/body//a[contains(@href,'register')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']").send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(generate_email())
    time.sleep(2)
    driver.find_element_by_xpath("//a[@active-class='active']").click()
    time.sleep(10)


def test_cookie1():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("http://localhost:1667")

    cookies = driver.find_element_by_xpath("//div/div[2]/button[2]/div")

    print(cookies.is_displayed())
    print(cookies.is_enabled())

    print(driver.get_cookies())
    time.sleep(1)

    accept = driver.find_element_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]/button[2]/div")
    accept.click()

    print(driver.get_cookies())

    time.sleep(10)
    driver.get("https://www.python.org/")
    time.sleep(5)
    driver.close()
    time.sleep(3)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("http://localhost:1667/#/")
    time.sleep(5)
    print(driver.get_cookies())
    time.sleep(2)
    driver.close()
    time.sleep(2)





