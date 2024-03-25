import praw
import csv

# Initialize Reddit instance
reddit = praw.Reddit(client_id='7FohD193NCbs_69fBdgzNw',
                     client_secret='QVgSVj3ym1sGMEebp_oxF7mniR2Nrg',
                     user_agent='Common_Part3970')

# Specify the subreddit
subreddit = reddit.subreddit('DeepFakeOne')

# Specify the fields you want to retrieve
fields = ['title', 'score', 'url', 'created_utc']

# Open a CSV file to write the data
with open('deepfakeone.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    # Iterate through the top posts in the subreddit
    for submission in subreddit.top(limit=100):  # Adjust limit as needed
        writer.writerow({field: getattr(submission, field) for field in fields})
