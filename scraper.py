import requests
from bs4 import BeautifulSoup
import re


def scrape_website(url, num_letters):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object with the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all text content within HTML tags
        text = soup.get_text()

        # Use regular expressions to find words
        # with the specified number of letters
        pattern = r'\b[a-zA-Z]{' + str(num_letters) + r'}\b'
        words = re.findall(pattern, text)

        # Return the list of words with the specified number of letters
        return words
    else:
        # If the request was not successful, print an error message
        print("Error: Failed to retrieve the website content.")
        return []


# URL of the website to scrape
website_url = 'https://www.dictionary.com/e/word-finder/4-letter-words/'

# Ask the user for the number of letters to look for
num_letters = int(input("Enter the number of letters to search for: "))

# Scrape the website for words with the specified number of letters
result = scrape_website(website_url, num_letters)

# Print the extracted words
for word in result:
    print(word)
