from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    def test_login(emil, password):
        driver.get("http://localhost:1667/#/")

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

    def test_logout():

        logout = driver.find_element_by_xpath("//a [@active-class='active']")
        print(logout.is_enabled())
        print(logout.is_displayed())
        logout.click()
        time.sleep(2)
        while True:
            try:
                logout.is_enabled()
                print("Látható")
            except:
                print("Nem látható az oldalon")
                break

    test_logout()
finally:
    pass
    #driver.close()
