from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:1667/#/")

    navbar = driver.find_elements_by_class_name("ion-compose")
    print(navbar)

    element = driver.find_element_by_xpath("/html/body//a[contains(@href,'login')]")
    print(element.is_enabled())
    print(element.is_displayed())

    element.click()
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys("tkata@gmail.com")
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys("Sunshine2046")
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(2)

    continue_link = driver.find_element_by_xpath("//ul/li[2]").click()

    article = driver.find_element_by_xpath("//input[@type='text'][@placeholder='Article Title']")
    article.send_keys("Spring")
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='What's this article about?']").send_keys("About my favorite season")
    driver.find_element_by_xpath("//input[@rows='8'][@placeholder='Write your article (in markdown)']").send_keys("Spring is my life")
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Enter tags')']").send_keys("Spring is my life")

    driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

finally:
    pass
    #driver.close()


#user send key-el kitölti ...miért nem tudom kitölteni?
#user click publish button
#assert home oldalon, hogy a cikk látható-e, kattintható-e, elérhető-e
