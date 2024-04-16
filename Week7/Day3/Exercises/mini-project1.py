from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://www.inmotionhosting.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(4)

host_plans_details = driver.find_elements(By.CLASS_NAME, 'imh-rostrum-card')

plan_list = []
for idx, plan in enumerate(host_plans_details, start=1):
    plan_name = plan.find_element(By.XPATH, './/h3').text
    plan_features = plan.find_element(By.XPATH, './/div[1]').text
    # Generate XPath for price dynamically based on index
    plan_price_xpath = f'//*[@id="home-rostrum-3"]/div/div/div[{idx}]/div[2]/div[1]/div'
    try:
        plan_price = plan.find_element(By.XPATH, plan_price_xpath).text
    except NoSuchElementException:
        plan_price = "Price not found"
    
    plan_item = {
        'Name': plan_name,
        'Feature': plan_features,
        'Price': plan_price
    }
    plan_list.append(plan_item)


df = pd.DataFrame(plan_list)
print(df)

driver.quit()  # Close Selenium WebDriver