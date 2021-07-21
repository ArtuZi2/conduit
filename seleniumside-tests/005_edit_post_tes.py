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
    def test_login(emil, password):

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

    test_login("tkata@gmail.com", "Sunshine2046")

    continue_link = driver.find_element_by_xpath("//a[@href='#/editor']").click()

    def test_new_post(title, lead, szoveg, tag):

        time.sleep(2)
        article = driver.find_element_by_xpath("//fieldset[1]/input").send_keys(title)
        time.sleep(3)
        lead = driver.find_element_by_xpath("//fieldset[2]/input").send_keys(lead)
        time.sleep(2)
        szoveg = driver.find_element_by_xpath("//fieldset[3]/textarea").send_keys(szoveg)
        time.sleep(2)
        tag = driver.find_element_by_xpath("//fieldset[4]/div/div/ul/li/input").send_keys(tag)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()
        time.sleep(2)

    test_new_post("Spring", "About my favorite season", "Spring is my life.", "Spring\n")
    driver.back()

    def test_edit_post(title, lead, szoveg, tag):
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[1]/input").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[1]/input").send_keys(title)
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[2]/input").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[2]/input").send_keys(lead)
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[3]/textarea").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[3]/textarea").send_keys(szoveg)
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[4]/div/div/ul/li/input").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset[4]/div/div/ul/li/input").send_keys(tag)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()

    test_edit_post("Winter", "About my favorite season", "Winter is the best.", "Winter\n")
    driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/button")
finally:
    pass

#függvénybe tenni
#dry, helyretenni az ismétléseket
#tagek törlése
#cikk ellenőrzése, hogy megjelenik-e a home és a my article oldalon
