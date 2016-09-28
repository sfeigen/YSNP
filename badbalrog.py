import tweepy
from config import *
from password_generator import *

import json
from tweepy import Stream
from tweepy.streaming import StreamListener

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(auth)

class listener(StreamListener):

    def on_data(self, data):
        test_str = json.loads(data)['text'][17:]  
        user = json.loads(data)['user']['screen_name']

        #go to p/w gen and run alg
        multiplier_val = multiplier(test_str)
        response = value_router(test_str)

        #generate tweet based upon results
        tweet = "@" + user + " " + response
        api.update_status(tweet)

        return(True)

    #grab status
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print status
        

# payload = generate()
# API.update_status(payload)