from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.chrome.options import Options
options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


@pytest.mark.order(1)
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


@pytest.mark.order(2)
def test_listazas():
    titles = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div/a/h1')

    try:
        titles_count = 0
        with open('titles.txt', 'w') as text_file:
            for title in titles:
                text_file.write(f'{title.text}\n')
                titles_count += 1

        print(f'number of links found on the page: {titles_count}')
    finally:
        pass
        driver.close()
        driver.quit()


test_listazas()

