from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:1667/#/")
driver.find_element_by_xpath("/html/body//a[contains(@href,'register')]").click()
driver.find_element_by_xpath("//input[@type='text'][@placeholder='Username']").send_keys("sun")
driver.find_element_by_xpath("//input[@type='text'][@placeholder='Email']").send_keys("tkata@gmail.com")
driver.find_element_by_xpath("//input[@type='password'][@placeholder='Password']").send_keys("Sunshine2046")
driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']").click()

#assert megjelenik-e a home oldal, illetve a session, megjelenik-e a username

"""except

finally:
pass

#driver.close"""
