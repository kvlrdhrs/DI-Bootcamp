from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import numpy as np
import re
import pandas as pd
import time

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
service = Service(executable_path="C:/chromedriver")  

driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the weather forecast page for a specific city
city = "New York"
url = f"https://weather.com/weather/tenday/l/{city}"
driver.get(url)

# Give the page time to load dynamically
time.sleep(5)  # Adjust sleep time if necessary

# Extract the HTML content
html_content = driver.page_source
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract weather forecast data
forecasts = soup.find_all("details", class_="Disclosure--themeList--uBa5q")

temperatures = []
conditions = []
humidities = []

for forecast in forecasts:
    try:
        temp = forecast.find("span", class_="DetailsSummary--highTempValue--3x6cL").text
        condition = forecast.find("span", class_="DetailsSummary--extendedData--aaFeV").text
        humidity = forecast.find("span", class_="DetailsTable--value--1F3Ze").text

        # Convert temperature to a float and remove the degree symbol
        temp_value = float(re.search(r"(\d+)", temp).group(1))
        temperatures.append(temp_value)
        conditions.append(condition)
        humidities.append(humidity)
    except AttributeError:
        continue

# Ensure all lists are the same length
min_length = min(len(temperatures), len(conditions), len(humidities))
temperatures = temperatures[:min_length]
conditions = conditions[:min_length]
humidities = humidities[:min_length]

# Calculate the average temperature
average_temp = np.mean(temperatures)

# Identify the most common weather condition
common_condition = max(set(conditions), key=conditions.count)

# Print the analysis results
print(f"Average Temperature: {average_temp:.2f}°F")
print(f"Most Common Weather Condition: {common_condition}")

# Create a DataFrame for further analysis
data = {
    "Temperature": temperatures,
    "Condition": conditions,
    "Humidity": humidities
}

df = pd.DataFrame(data)
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv("weather_data.csv", index=False)
