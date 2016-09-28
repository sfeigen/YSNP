import tweepy
from config import *
from password_generator import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(auth)

multiplier_val = multiplier(test_str)
test_str = value_router(test_str)

class listener(StreamListener):

    def on_data(self, data):
        text = json.loads(data)['text'][15:]  
        user = json.loads(data)['user']['screen_name']

        #logic goes here
        new_password = generate_password()
        tweet = "@" + user + " " + new_password

        tweetBack(tweet)

        return(True)

    #grab status
    def on_status(self, status):
        print(status.text)

    def on_error(self, status):
        print status
        

# payload = generate()
# API.update_status(payload)