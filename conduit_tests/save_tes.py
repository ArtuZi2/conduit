from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())


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


test_login()


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
    df = pd.DataFrame(data_list)

    # saving the dataframe to a csv
    df.to_csv('table.csv')
    driver.close()


test_save()



