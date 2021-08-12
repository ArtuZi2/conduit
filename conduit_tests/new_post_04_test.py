from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random, string
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

"""@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:1667/#/")
    return driver"""


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

    time.sleep(2)

    driver.find_element_by_xpath("//a[@active-class='active']").click()


def test_login():
    driver.get("http://localhost:1667")
    time.sleep(2)

    element = driver.find_element_by_xpath("//div/nav/div/ul/li[2]/a")
    emil = "tkata@gmail.com"
    password = "Sunshine2046"

    element.click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(emil)
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(5)

# New Article button
    driver.find_element_by_xpath("//nav/div/ul/li[2]/a").click()


def home():

    driver.find_element_by_xpath("//nav/div/ul/li[1]/a").click()
    time.sleep(5)

    my_feed = driver.find_element_by_xpath("//div/div/div/div/div/div/ul/li/a")
    my_feed.click()


def test_check1():
    time.sleep(5)
    titles = driver.find_elements_by_xpath('//div/div[2]/div/div[1]/div[2]/div/div/div/a/h1')

    titles_list1 = []

    titles_count1 = 0
    time.sleep(5)
    with open('titles1.txt', 'w') as text_file:
        for title in titles:
            text_file.write(f'{title.text}\n')
            titles_count1 += 1
            titles_list1.append(title)

    print(f'number of links found on the page: {titles_count1}')
    print(len(titles))
    print(len(titles_list1))


def test_new_post():
    time.sleep(2)
    driver.get("http://localhost:1667/#/editor")
    time.sleep(5)
    article = driver.find_element_by_xpath("//fieldset[1]/input")
    article.send_keys("Spring")
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys("About my favorite season")
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[3]/textarea").send_keys("Spring is my life.")
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[4]/div/div/ul/li/input").send_keys("Spring\n", "life\n", "season\n",
                                                                                "favorite\n")
    time.sleep(5)
    driver.find_element_by_xpath("//div/div/div/div/form/button").click()

    time.sleep(5)


def home():

    driver.find_element_by_xpath("//nav/div/ul/li[1]/a").click()
    time.sleep(5)

    my_feed = driver.find_element_by_xpath("//div/div/div/div/div/div/ul/li/a")
    my_feed.click()


time.sleep(5)


def test_check2():
    time.sleep(5)
    titles = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div/a/h1')

    titles_list2 = []

    titles_count2 = 0
    time.sleep(5)
    with open('titles.txt', 'w') as text_file:
        for title in titles:
            text_file.write(f'{title.text}\n')
            titles_count2 += 1
            titles_list2.append(title)

    print(f'number of links found on the page: {titles_count2}')
    print(len(titles))
    print(len(titles_list2))

    assert len(titles) == len(titles_list2)
