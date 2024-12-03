from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from random import randint
from os import path
import time

display = Display(visible=0, size=(800, 600))
display.start()

firefox_options = webdriver.FirefoxOptions()

firefox_options.headless = True

driver = webdriver.Firefox(options=firefox_options)

driver.get("https://www.alza.cz")

main_links = [
    element.get_attribute("href")
    for element in driver.find_elements(By.CLASS_NAME, "l0-catLink")
]

categories_que = []

for link in main_links:
    time.sleep(randint(1, 9) / 10)

    driver.get(link)

    categories_que.extend(
        [
            element.get_attribute("href")
            for element in driver.find_elements(By.CLASS_NAME, "category-tiles__tile")
        ]
    )

    print(len(categories_que), categories_que)
    time.sleep(randint(1, 9) / 10)

# driver.get("https://www.alza.cz/alzaplus-slevy/e19.htm")

# with open(path.join(path.dirname(path.realpath(__file__)), "index.html"), "w") as f:
#     f.write(driver.page_source)

driver.quit()
display.stop()

print(categories_que)
