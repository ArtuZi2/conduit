from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random, string
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


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

    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a [@active-class='active']").click()
    time.sleep(2)


def test_login():
    emil = "tkata@gmail.com"
    password = "Sunshine2046"

    driver.get("http://localhost:1667/#/")
    time.sleep(2)
    element = driver.find_element_by_xpath("//a[@href='#/login']")
    element.click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(emil)
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(2)


def test_save():
    settings = driver.find_element_by_xpath("//a[@href='#/settings']")
    settings.click()
    time.sleep(2)
    data_list = []
    username = driver.find_element_by_xpath("//fieldset[2]/input")
    emil = driver.find_element_by_xpath("//fieldset[4]/input")

    table_dict = {'Username': username.text,
                  'Email': emil.text}

    data_list.append(table_dict)
    df = pandas.DataFrame(data_list)

    df.to_csv('table.csv')



