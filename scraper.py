import requests
from bs4 import BeautifulSoup
import re


def scrape_website(url, num_letters):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        pattern = r'\b[a-zA-Z]{' + str(num_letters) + r'}\b'
        words = re.findall(pattern, text)
        return words
    else:
        print("Error: Failed to retrieve the website content.")
        return []


website_url = 'https://www.example.com/'
num_letters = int(input("Enter the number of letters to search for: "))
result = scrape_website(website_url, num_letters)

for word in result:
    print(word)
