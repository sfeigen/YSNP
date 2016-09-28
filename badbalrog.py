import tweepy
from config import *
from password_generator import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(auth)

multiplier_val = multiplier(test_str)
print(password_value(test_str))

# payload = generate()
# API.update_status(payload)