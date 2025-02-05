import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape Reddit's r/python subreddit
def scrape_reddit_python():
    # Base URL for r/python
    base_url = "https://www.reddit.com/r/python/"