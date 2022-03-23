import tweepy
import os
from dotenv import load_dotenv
import datetime
import time

load_dotenv()

auth = tweepy.OAuth1UserHandler(str(os.getenv('consumer_key')), str(os.getenv('consumer_key_secret')), str(os.getenv('access_token')), str(os.getenv('access_token_secret')))
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_tweets(word):
    date_only = datetime.datetime.now().date()
    for tweet in tweepy.Cursor(api.search_tweets, q=word, count=100, tweet_mode='extended', until = date_only).items():
        text = tweet._json["full_text"]
        print(text)
        id = tweet._json["id"]
        responed_to_tweet(id)
        time.sleep(10)
        print('\n\n')

def get_trends():
    trends = tweepy.API
    print(trends.get_place_trends(id=int(os.getenv('WOE_ID'))))

def get_keywords():
    path = "./"
    obj = os.scandir()
    for entry in obj:
        if entry.is_file():
            if '.txt' in str(entry.name):
                read_file(str(entry.name))
                

def read_file(file):
    with open(file) as f:
        lines = f.readlines()
        for word in lines:
            get_tweets(str(word))

def responed_to_tweet(id):
    tweepy.Client.create_tweet(text="hello", quote_tweet_id=id)

while True:
    #get_trends()
    get_keywords()