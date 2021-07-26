from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())

"""@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:1667/#/")
    return driver"""

def test_login():
    navbar = driver.find_elements_by_class_name("ion-compose")
    print(navbar)

    element = driver.find_element_by_xpath("/html/body//a[contains(@href,'login')]")
    print(element.is_enabled())
    print(element.is_displayed())
    emil = "tkata@gmail.com"
    password = "Sunshine2046"

    element.click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(emil)
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(2)

#New Article button
continue_link = driver.find_element_by_xpath("//a[@href='#/editor']").click()

def test_new_post():

    time.sleep(2)
    article = driver.find_element_by_xpath("//fieldset[1]/input")
    article.send_keys("Spring")
    time.sleep(3)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys("About my favorite season")
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[3]/textarea").send_keys("Spring is my life.")
    time.sleep(2)
    driver.find_element_by_xpath("//fieldset[4]/div/div/ul/li/input").send_keys("Spring\n", "life\n", "season\n",
                                                                                "favorite\n")
    time.sleep(4)
    driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

time.sleep(2)

my_feed = driver.find_element_by_xpath("//a[@href='#/my-feed']")
my_feed.click()


"""def test_delete_post():
    delete_button = driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']")
    delete_button.click()
    driver.find_elements_by_tag_name('button')[2].click()"""


#assert home és my article oldalon, hogy a cikk látható-e, kattintható-e, elérhető-e
