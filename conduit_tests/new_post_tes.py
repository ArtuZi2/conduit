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
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)

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

    """print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)"""


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
    driver.find_element_by_xpath("//a[@href='#/editor']").click()


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
    #home
    driver.find_element_by_xpath("//nav/div/ul/li[1]/a").click()

    my_feed = driver.find_element_by_xpath("//a[@href='#/my-feed']")
    my_feed.click()

    article_title = "Spring"
    assert

    def test_listazas():
        titles = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div/a/h1')

        titles_count = 0
        with open('titles.txt', 'w') as text_file:
            for title in titles:
                text_file.write(f'{title.text}\n')
                titles_count += 1

            print(f'number of links found on the page: {titles_count}')



"""def test_delete_post():
    delete_button = driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']")
    delete_button.click()
    driver.find_elements_by_tag_name('button')[2].click()"""


#assert home és my article oldalon, hogy a cikk látható-e, kattintható-e, elérhető-e
