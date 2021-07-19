from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install())


extracted_data = []
driver = webdriver.Chrome(ChromeDriverManager().install())

def test_bejaras():
    driver.get("driver.get("http://localhost:1667/#/")")
    while True:
        table = driver.find_element_by_xpath("")
        rows = driver.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = driver.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

        pprint.pprint(extracted_data)
        print(len(extracted_data))

    test_bejaras()bejaras()

finally:
    pass
    #driver.close()