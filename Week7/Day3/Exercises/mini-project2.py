from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from bs4 import BeautifulSoup


# Switch to the iframe

# //*[@id="iframe"] - path for iframe
# /html/body/div[1]/div[1]/h3 - path for turtle_name


def webscrap(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(4)

    driver.switch_to.default_content()
    iframe = driver.find_element(By.XPATH, '//*[@id="iframe"]')
    driver.switch_to.frame(iframe)

    page = BeautifulSoup(driver.page_source, 'html')
    
    for turtle in soup:
        turtles = driver.find_elements(By.CLASS_NAME, 'col-md-4 turtle-family-card')


for movie in movies:
    title = [item.get_text() for item in soup.find_all(class_ = 'p--small')]




# url = 'https://www.scrapethissite.com/pages/frames/'