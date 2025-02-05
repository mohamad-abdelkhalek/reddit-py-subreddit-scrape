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