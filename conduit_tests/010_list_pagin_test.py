from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
import pprint
import pytest_order
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


@pytest.mark.order(1)
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
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a").click()
    time.sleep(2)
    user_setting = driver.find_element_by_tag_name("h4")
    time.sleep(2)
    print(user_setting.text)
    user = "sun2"

    assert user == user_setting.text

    driver.find_element_by_xpath("//a [@active-class='active']").click()

    print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("https://www.google.com/")
    except Exception as e:
        print(e)


test_login()


extracted_data = []


@pytest.mark.order(2)
def test_pagin():
    article_title_list = []
    page_count = 1

    while True:
        time.sleep(2)
        article_titles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        for article in article_titles:
            article_title_list.append(article.text)
        try:
            page_count += 1
            driver.find_element_by_link_text(str(page_count)).click()
        # driver.find_element_by_xpath('//*[@id="app"]//nav/ul/li[%]/a')
        except:
            # Stop loop if no more page available
            break

    print("The title-list of My Article: ", article_title_list)
    print("Number of My article: ", len(article_title_list))

    # Writting to csv file:
    article_count = 0
    with open('titles.csv', 'w', encoding='utf-8') as file:
        for title in article_title_list:
            file.write(f'{article_title_list}')
            article_count += 1

    # Comparing the number of the saved titles with number of the Article feed titles:
    assert int(len(article_title_list)) == int(article_count)

    print("Current session is {}".format(driver.session_id))
    driver.close()
    try:
        driver.get("https://www.google.com/")
    except Exception as e:
        print(e)


test_pagin()
