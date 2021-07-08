from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


def register(username, email, password):
    driver.get("http://localhost:1667/#/")
    driver.find_element_by_xpath("/html/body//a[contains(@href,'register')]").click()
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']").send_keys(username)
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys(email)
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys(password)

    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(5)

    welcome = driver.find_element_by_xpath("//div[contains(@class, 'swal-text')]").text
    text = "Your registration was successful!"
    assert (text == welcome)

    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()

    time.sleep(5)

    driver.find_element_by_xpath("//a[contains(@href, 'settings')]").click()

    megjelen_username = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a").text
    username = driver.find_element_by_xpath("//input[@type='text'][@placeholder='Your username']").text

    print(megjelen_username)

    assert(megjelen_username == username)

    driver.close


register("sun3", "tkata1@gmail.com", "Sunshine2046")

"""try:
    driver.get("http://localhost:1667/#/")
    driver.find_element_by_xpath("/html/body//a[contains(@href,'register')]").click()
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']").send_keys("sun")
    driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys("tkata@gmail.com")
    driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys("Sunshine2046")
    driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

    time.sleep(10)

    welcome = driver.find_element_by_xpath("//div[contains(@class, 'swal-text')]").text
    text = "Your registration was successful!"
    assert(text == welcome)

    driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
    sun = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
    username = driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']")

    assert(sun == username)

finally:
    pass
    # driver.close"""
