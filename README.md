# Reddit r/python Data Collector

A Python script that uses the Reddit API to collect and analyze posts from the r/python subreddit. This tool fetches information such as post titles, scores, comment counts, and creation timestamps, saving the data in a CSV format for further analysis.

## Features

- Fetches hot posts from r/python subreddit
- Collects comprehensive post data including:
  - Post titles
  - URLs
  - Upvote scores
  - Comment counts
  - Creation timestamps
- Saves data to timestamped CSV files
- Respects Reddit's API rate limits
- Uses secure environment variables for API credentials

## Prerequisites

- Python 3.6 or higher
- Reddit account
- Reddit API credentials (client ID and client secret)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mohamad-abdelkhalek/reddit-python-scraper.git
cd reddit-python-scraper
```

2. Install required packages:
```bash
pip install praw python-dotenv
```

3. Set up your Reddit API credentials:
   - Go to https://www.reddit.com/prefs/apps
   - Click "create another app..."
   - Fill in the following details:
     - Name: Your app name
     - Type: Select "script"
     - Description: Brief description of your script
     - About URL: Can be left blank
     - Redirect URI: http://localhost:8080

4. Create a `.env` file in the project root directory:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
```

## Usage

Run the script using:
```bash
python scrape_reddit_python.py
```

The script will:
1. Connect to Reddit using your API credentials
2. Fetch the latest hot posts from r/python
3. Save the data to a CSV file with a timestamp in the filename
4. Display the collected data in the console

## Output Format

The script generates a CSV file with the following columns:
- Title: Post title
- Link: Full URL to the post
- Score: Number of upvotes
- Comments: Number of comments
- Created: Post creation timestamp

Example output filename: `reddit_python_20240205_143022.csv`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- [PRAW Documentation](https://praw.readthedocs.io/)
- Reddit API Terms of Service
- Python subreddit community

## Safety Note

Remember to:
- Never commit your `.env` file to version control
- Keep your Reddit API credentials secure
- Follow Reddit's API terms of service and usage guidelines
- Respect rate limits and data usage policies

## Support

For support, please:
1. Check existing issues in the repository
2. Create a new issue with detailed information if your problem hasn't been reported
3. Include relevant error messages and steps to reproduce any problems
