from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
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
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']").send_keys(username)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(generate_email())
    # if driver.find_element_by_class_name("swal-modal").is_displayed():
    #  a = driver.find_element_by_class_name("swal-button swal-button--confirm")
    #   a.click()
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)

    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(5)

    welcome = driver.find_element_by_xpath("//div[contains(@class, 'swal-text')]").text
    text = "Your registration was successful!"
    assert (text == welcome)

    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()

    driver.find_element_by_xpath("//a [@active-class='active']").click()

    """print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)"""


def test_login():
    emil = "tkata@gmail.com"
    password = "Sunshine2046"

    driver.get("http://localhost:1667")
    time.sleep(2)

    element = driver.find_element_by_xpath("//a[@href='#/login']")

    element.click()
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[1]/input").send_keys(emil)
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()


def test_new_post():

    #new_article
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='#/editor']").click()
    time.sleep(2)
    article = driver.find_element_by_xpath("//fieldset[1]/input")
    article.send_keys("Autumn")
    time.sleep(3)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys("About my favorite season")
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[3]/textarea").send_keys("Autumn is my life.")
    time.sleep(4)
    driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()
    time.sleep(5)


def test_delete_post():
    time.sleep(5)
    delete_button = driver.find_element_by_xpath("//div/div[1]/div/div/span/button")
    delete_button.click()

    time.sleep(5)

    driver.back()
    time.sleep(5)

    article_title = driver.find_element_by_xpath("//div/div[1]/div/h1")

    article_title.is_enabled()
    assert article_title == "Autumn"



#ellenőrizni, hogy kitörölte-e a cikket
#back aktiválása után ismét ellenőrizni