"""

import tweepy
import webbrowser
import time



consumer_key = ""
consumer_secret = ""
callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pin_input = input("What's the pin? ")
auth.get_access_token(user_pin_input)

api = tweepy.API(auth)

me = api.me()

print(me.screen_name)

"""