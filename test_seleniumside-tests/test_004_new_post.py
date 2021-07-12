from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

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

driver.find_element_by_xpath(("//a[@href, 'editor')]")).click()


#rákattintani new article
#assert megjelenik-e cím, lead, szöveg, tagek
#user send key-el kitölti
#user click publish button
#assert home oldalon, hogy a cikk látható-e, kattintható-e, elérhető-e
