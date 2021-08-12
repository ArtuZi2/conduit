from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import random, string
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
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

    # if driver.find_element_by_class_name("swal-modal").is_displayed():
    #  a = driver.find_element_by_class_name("swal-button swal-button--confirm")
    #   a.click()

    # belépés
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)

    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(5)
    welcome = driver.find_element_by_xpath("//div[contains(@class, 'swal-text')]").text
    text = "Your registration was successful!"
    assert (text == welcome)

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
    driver.find_element_by_xpath("//fieldset[1]/input").send_keys(emil)
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//div/div/div/div/form/button").click()

    time.sleep(5)
    driver.get("http://localhost:1667/#/editor")


def fill_article(xpath):
    element = driver.find_element_by_xpath(xpath)
    element.clear()
    time.sleep(2)
    return element


time.sleep(3)

with open('./articles.csv', encoding='utf-8') as csv_table:
    csv_reader = csv.reader(csv_table, delimiter=',')
    next(csv_reader)
    time.sleep(5)
    for row in csv_reader:
        print(row)
        fill_article("//fieldset/input").send_keys(row[0])
        time.sleep(5)
        fill_article("//fieldset[2]/input").send_keys(row[1])
        time.sleep(5)
        fill_article("//form/fieldset/fieldset[3]/textarea").send_keys(row[2])
        time.sleep(5)
        driver.find_element_by_xpath("//div/div/div/div/form/button").click()
        time.sleep(5)
        driver.get("http://localhost:1667/#/editor")
        time.sleep(5)
