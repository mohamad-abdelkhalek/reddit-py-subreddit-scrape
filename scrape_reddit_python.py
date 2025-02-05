import praw
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

def scrape_reddit_python():
    # Load environment variables
    load_dotenv()
    
    # Initialize Reddit API client
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent="Python:DataCollector:v1.0 (by /u/YOUR_USERNAME)"
    )
    
    # Access the Python subreddit
    subreddit = reddit.subreddit('python')
    
    # Prepare data list
    data = []
    
    # Get hot posts from r/python
    for post in subreddit.hot(limit=25):
        data.append([
            post.title,
            f"https://www.reddit.com{post.permalink}",
            post.score,
            post.num_comments,
            datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    # Save to CSV file
    filename = f"reddit_python_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link", "Score", "Comments", "Created"])
        writer.writerows(data)
    
    print(f"Data saved to {filename}")
    
    # Print the data to console
    for index, item in enumerate(data, start=1):
        print(f"\n{index}. Title: {item[0]}")
        print(f"   Link: {item[1]}")
        print(f"   Score: {item[2]}")
        print(f"   Comments: {item[3]}")
        print(f"   Created: {item[4]}")

if __name__ == "__main__":
    scrape_reddit_python()