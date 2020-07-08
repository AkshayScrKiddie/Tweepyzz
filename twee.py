import tweepy
from tweepy import OAuthHandler
import json
import re
from googletrans import Translator                          #For Translating tweets text to English words

access_token = "1128179205055770626-3nCdtumgBGx1gdDRa1pTsvTWtGAC4q"
access_token_secret = "4Vv3FYQAuKyBESawl3YBKRfK4rK6xiI28tJ2CGPwnBIon"
consumer_key = "Of9W5ZDCiHKxXUx8P769BTVra"
consumer_secret = "j67ROBreNNstCl8pFMlAzekup3L3l8MtZ0XHJXGnJoW0a1O03I"

translator = Translator()

class Twitter:

    def __init__(self,searchQuery):
        self.searchQuery=searchQuery

    def doit(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

        with open("results.json", 'a') as f:
           
            for tweet in tweepy.Cursor(api.search,q=self.searchQuery+"-filter:retweets").items(20000):
                    tweet.text = re.sub('@[^\s]+','',tweet.text)
                    json.dump(tweet._json, f)
                    f.write('\n')      
                       
listener = Twitter('#bjp' or '#modi')
listener.doit()