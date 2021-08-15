from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random, string
from selenium.webdriver.chrome.options import Options
import pytest_order
import pytest

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# regisztráció random email címmel

@pytest.mark.order1
def test_register():
    username = "sun2"
    password = "Sunshine2046"
    e_mail = "tkata@gmail.com"

    driver.get("http://localhost:1667")

    """def generate_email(prefix='tkata+', domain='gmail.com'):
        random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                              for _ in range(10))

        return prefix + random_part + '@' + domain

    generate_email()"""

    time.sleep(5)
    driver.find_element_by_xpath("/html/body//a[contains(@href,'register')]").click()
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']").send_keys(username)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(e_mail)
    # if driver.find_element_by_class_name("swal-modal").is_displayed():
    #  a = driver.find_element_by_class_name("swal-button swal-button--confirm")
    #   a.click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)

    # belépés

    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(5)

    #W welcome üzenet elfogadása

    welcome = driver.find_element_by_xpath("//div[contains(@class, 'swal-text')]").text
    text = "Your registration was successful!"
    assert (text == welcome)

    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()

    time.sleep(5)

    megjelen_username = driver.find_element_by_xpath(f"//a[contains(@href, '@sun2')]").text

    print(megjelen_username)

    # felhasználónév összahasonlítása a bevitt felhasználónévvel

    assert megjelen_username == username

    time.sleep(5)

    driver.find_element_by_xpath("//a[@active-class='active']").click()

