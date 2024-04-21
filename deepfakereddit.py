import praw
import csv
from textblob import TextBlob
from datetime import datetime

# Initialize Reddit instance
reddit = praw.Reddit(client_id='7FohD193NCbs_69fBdgzNw',
                     client_secret='QVgSVj3ym1sGMEebp_oxF7mniR2Nrg',
                     user_agent='Common_Part3970')

# Specify the subreddit
subreddit = reddit.subreddit('DeepFakeOne')

# Specify the fields you want to retrieve
fields = ['title', 'score', 'url', 'created_utc', 'num_comments', 'ups', 'downs']

# Open a CSV file to write the data
with open('reddit_data_with_features.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    # Iterate through the top posts in the subreddit
    for submission in subreddit.top(limit=100):  # Adjust limit as needed
        title = submission.title
        score = submission.score
        url = submission.url
        created_utc = submission.created_utc
        num_comments = submission.num_comments
        ups = submission.ups
        downs = submission.downs

        # Perform sentiment analysis on the title
        title_blob = TextBlob(title)
        title_sentiment = title_blob.sentiment.polarity

        # Calculate word count and average word length of the title
        words = title.split()
        word_count = len(words)
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0

        # Derive posting date and time from created_utc timestamp
        posting_datetime = datetime.utcfromtimestamp(created_utc).strftime('%Y-%m-%d %H:%M:%S')

        # Write the data to the CSV file
        writer.writerow({
            'title': title,
            'score': score,
            'url': url,
            'created_utc': posting_datetime,
            'num_comments': num_comments,
            'ups': ups,
            'downs': downs,
            'title_sentiment': title_sentiment,
            'word_count': word_count,
            'avg_word_length': avg_word_length
        })
