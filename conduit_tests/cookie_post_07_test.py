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
    # if driver.find_element_by_class_name("swal-modal").is_displayed():
    #  a = driver.find_element_by_class_name("swal-button swal-button--confirm")
    #   a.click()
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)
    time.sleep(2)

    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(5)

    welcome = driver.find_element_by_xpath("//div[contains(@class, 'swal-text')]").text
    text = "Your registration was successful!"
    assert (text == welcome)

    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()

    time.sleep(5)

    # driver.find_element_by_xpath("//a[contains(@href, 'settings')]").click()

    # appear_name = driver.find_elements_by_xpath("//a[@href]")

    # megjelen_username = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a").text

    # megjelen_username = driver.find_element_by_xpath("//a[contains(@href, '@sun2')]").text

    megjelen_username = driver.find_element_by_xpath(f"//a[contains(@href, '@sun2')]").text
    # driver.find_element_by_xpath("//fieldset[2]/input[@type='text']").send_keys("emma")

    print(megjelen_username)
    # print(username)

    assert megjelen_username == username

    time.sleep(2)

    driver.find_element_by_xpath("//a [@active-class='active']").click()
    time.sleep(10)


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


def test_cookie1():

    driver.get("http://localhost:1667/#/")

    time.sleep(1)

    cookies = driver.find_element_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]")

    print(cookies.is_displayed())
    print(cookies.is_enabled())

    print(driver.get_cookies())
    time.sleep(1)

    accept = driver.find_element_by_xpath("//*[@id='cookie-policy-panel']/div/div[2]/button[2]/div")
    accept.click()

    print(driver.get_cookies())

    time.sleep(2)

    driver.get("https://www.python.org/")
    time.sleep(2)
    driver.close()
    driver.get("http://localhost:1667/#/")
    time.sleep(2)
    print(driver.get_cookies())
    time.sleep(2)
    driver.close()
    time.sleep(2)

    """print("Current session is {}".format(driver.session_id))
    driver.close()

    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)"""





