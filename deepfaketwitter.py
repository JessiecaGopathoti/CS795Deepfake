import tweepy
import csv

# Twitter API credentials
consumer_key = 'rAz48Ojp5OEUGtk7lECea2ub1'
consumer_secret = 'LXcoTZW6zc5CE9As5fvG4xmPjZSbX1iVut9PXIyt1Q8SVR5tbD'
access_token = '1772285171175231489-oUXnardDs21tN7QdG1qcePsXZF7It2'
access_token_secret = 'WjDIR5qOzOH7zZapU65evoTXhRljWzcaUuoMK2iV82Y9N'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Specify the user or hashtag you want to retrieve tweets from
user_or_hashtag = 'DeepFakeOne'

# Specify the fields you want to retrieve
fields = ['text', 'favorite_count', 'retweet_count', 'created_at']

# Open a CSV file to write the data
with open('twitter_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    # Fetch tweets using Cursor
    for tweet in tweepy.Cursor(api.search_tweets, q=user_or_hashtag, tweet_mode='extended').items(100):
        writer.writerow({field: getattr(tweet, field) for field in fields})