import credentials
import tweepy
import time

from random import randint

NUM_OF_TWEETS = 10


class TweetAutomation:
    consumer_key = credentials.CONSUMER_KEY
    consumer_secret = credentials.CONSUMER_SECRET
    access_token = credentials.ACCESS_TOKEN
    access_token_secret = credentials.ACCESS_TOKEN_SECRET

    api = tweepy.API()

    WAIT_TIME = 30
    HASH_TAG = "#cmpe295A"
    messages = ["Fire", "Food", "Shelter", "Doctor"]

    def __init__(self):
        self.auth()

    def auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)

        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def send_tweet(self):
        idx = randint(0, len(self.messages) - 1)
        self.api.update_status(status=self.messages[idx] + " \n" + self.HASH_TAG)
        time.sleep(self.WAIT_TIME)


if __name__ == "__main__":
    tweet_automation = TweetAutomation()
    for i in range(NUM_OF_TWEETS):
        tweet_automation.send_tweet()
