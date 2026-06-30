import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    """Scrapes the title of a webpage given its URL."""
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise an error for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        return title
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"