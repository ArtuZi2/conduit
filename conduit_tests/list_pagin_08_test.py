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

    driver.get("http://localhost:1667")

    time.sleep(2)

    element = driver.find_element_by_xpath("//a[@href='#/login']")

    element.click()
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[1]/input").send_keys(emil)
    time.sleep(5)
    driver.find_element_by_xpath("//fieldset[2]/input").send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    """print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)"""


extracted_data = []


def test_pagin():
    article_title_list = []
    page_count = 1

    while True:
        time.sleep(5)
        article_titles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        for article in article_titles:
            article_title_list.append(article.text)
        try:
            page_count += 1
            driver.find_element_by_link_text(str(page_count)).click()
        except:
            break

    print("Titles: ", article_title_list)
    print("Titles's number: ", len(article_title_list))

    time.sleep(5)

    article_count = 0
    with open('titles.csv', 'w', encoding='utf-8') as file:
        for title in article_title_list:
            file.write(f'{article_title_list}')
            article_count += 1

    assert int(len(article_title_list)) == int(article_count)

    print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("http://localhost:1667")
    except Exception as e:
        print(e)
