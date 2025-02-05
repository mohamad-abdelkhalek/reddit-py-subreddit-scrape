import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape Reddit's r/python subreddit
def scrape_reddit_python():
    # Base URL for r/python
    base_url = "https://www.reddit.com/r/python/"
    
    # Headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send a GET request to the website
    response = requests.get(base_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all post containers
        posts = soup.find_all("div", attrs={"data-testid": "post-container"})
