import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
scraped_data = []
for i in range(len(quotes)):
    scraped_data.append({
        'Title/Quote': quotes[i].text,
        'Author/Category': authors[i].text
    })
df = pd.DataFrame(scraped_data)
df.to_csv('competitor_analysis.csv', index=False)
print("--- SCRAPED COMPETITOR DATA ---")
print(df.head())
print("\nSuccess! 'competitor_analysis.csv' created.")