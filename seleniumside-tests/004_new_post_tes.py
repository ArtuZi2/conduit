from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:1667/#/")
try:
    def login(emil, password):
        navbar = driver.find_elements_by_class_name("ion-compose")
        print(navbar)

        element = driver.find_element_by_xpath("/html/body//a[contains(@href,'login')]")
        print(element.is_enabled())
        print(element.is_displayed())

        element.click()
        driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(emil)
        driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)
        driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

        time.sleep(2)

    login("tkata@gmail.com", "Sunshine2046")

#New Article button
    continue_link = driver.find_element_by_xpath("//a[@href='#/editor']").click()

    def new_post():

        time.sleep(2)
        article = driver.find_element_by_xpath("//fieldset[1]/input")
        article.send_keys("Spring")
        time.sleep(3)
        #driver.find_element_by_xpath("//fieldset[2]/input"").send_keys("About my favorite season")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@rows='8'][@placeholder='Write your article (in markdown)']").send_keys("Spring is my life")
        time.sleep()
        driver.find_element_by_xpath("//input[@type='text'][@placeholder='Enter tags')']").send_keys("Spring is my life")

        driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

    new_post()
finally:
    pass
    #driver.close()


#user send key-el kitölti ...miért nem tudom kitölteni?
#user click publish button
#assert home oldalon, hogy a cikk látható-e, kattintható-e, elérhető-e
