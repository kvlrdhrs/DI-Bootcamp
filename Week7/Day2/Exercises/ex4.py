import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    data = []
    for article in articles:
        # Find the article name
        article_name = article.find('h3', class_='jsx-268a7bdb02dd195b card__headline')
        article_name_text = article_name.get_text(strip=True) if article_name else None

        # Find the time element containing the datetime
        time_element = article.find('time')
        datetime = time_element['datetime'] if time_element else None

        data.append({'Article_name': article_name_text, 'Article_date': datetime})

    return data

# Function to scrape data from multiple pages
def scrape_multiple_pages(base_url, max_pages):
    all_data = []
    for page_number in range(1, max_pages + 1):
        url = f"{base_url}/page/{page_number}"
        data = scrape_page(url)
        all_data.extend(data)
    return all_data

# Define the base URL and the maximum number of pages to scrape
base_url = "https://www.iranintl.com/en/archive/iran-en"
max_pages = 10

# Scrape data from multiple pages
all_data = scrape_multiple_pages(base_url, max_pages)

# Create a DataFrame
df = pd.DataFrame(all_data)

# Print the DataFrame
print(df)