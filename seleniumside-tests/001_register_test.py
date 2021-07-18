from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import random, string
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    def test_register(username, password):

        def generate_email(prefix='tkata+', domain='gmail.com'):
            random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                                  for _ in range(10))

            return prefix + random_part + '@' + domain

        generate_email()

        driver.get("http://localhost:1667/#/")
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

        megjelen_username = driver.find_element_by_xpath(f"//a[contains(@href, '@{username}')]").text
        # driver.find_element_by_xpath("//fieldset[2]/input[@type='text']").send_keys("emma")

        print(megjelen_username)
        # print(username)

        assert megjelen_username == username


    test_register("sun2", "Sunshine2046")

    driver.find_element_by_xpath("//ul/li[5]").click()

finally:
    driver.close()