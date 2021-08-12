from selenium import webdriver
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

    time.sleep(5)

    megjelen_username = driver.find_element_by_xpath(f"//a[contains(@href, '@sun2')]").text

    print(megjelen_username)
    # print(username)
    #felhasználónév összahasonlítása a bevitt felhasználónévvel
    assert megjelen_username == username

    time.sleep(2)

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
    div = driver.find_element_by_class_name("nav-item")
    navbar_items = div.find_elements_by_xpath("//div/nav/div/ul/li/a")
    list = []
    for i in navbar_items:
        list.append(i)
        print(i.text)

    time.sleep(2)

    element = driver.find_element_by_xpath("//a[@href='#/login']")
    print(element.is_enabled())
    print(element.is_displayed())

    element.click()
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[1]/input").send_keys(emil)
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//nav/div/ul/li[4]/a").click()
    time.sleep(5)
    user_setting = driver.find_element_by_tag_name("h4")
    time.sleep(5)
    print(user_setting.text)
    user = 'sun2'

    assert user == user_setting.text
    time.sleep(3)
    #navbar elemeinek megjelenítése belépés után
    driver.get("http://localhost:1667/#/")

    div = driver.find_element_by_class_name("nav-item")
    navbar_items = div.find_elements_by_xpath("//div/nav/div/ul/li/a")
    list2 = []
    for item in navbar_items:
        text = item.text
        list2.append(item)
        print(text)

    assert user == list2[3].text