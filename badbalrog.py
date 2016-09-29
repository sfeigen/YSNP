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
        #grab string after name
        password = json.loads(data)['text'][17:]  
        user = json.loads(data)['user']['screen_name']
        
        #go to p/w gen and run alg
        multiplier_val = multiplier(password)
        response = value_router(password)

        #update score
        strength = len(response) * multiplier(response)[0]

        if strength < 10:
            pass_comment = " ... this shall not pass...\n Password: "
        else:
            pass_comment = "\n Password is: "

        #generate tweet based upon results
        tweet = "@" + user + pass_comment + response + "\n With a Strength of: " + str(strength)
        API.update_status(tweet)

        return(True)

    #grab status
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print status
        
#track self
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['@nopasarassenior'], async=True)

# payload = generate()
# API.update_status(payload)