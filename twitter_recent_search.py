

import requests
from requests_oauthlib import OAuth1
import json
import tweepy


twitter = {
    "api_key" : "XXXXXX",
    "api_key_secret" : "XXXXXX",
    "access_token" : "XXXXXX",
    "access_token_secret" : "XXXXX"
}

api_key = twitter["api_key"]
api_key_secret  = twitter["api_key_secret"]

access_token = twitter["access_token"]
access_token_secret = twitter["access_token_secret"]
client = tweepy.Client(consumer_key=api_key,consumer_secret=api_key_secret,access_token=access_token,access_token_secret=access_token_secret)
auth = OAuth1(api_key,api_key_secret,access_token,access_token_secret)
response = requests.get("url",auth=auth)
t = response.json()
r = []
i = 1
for x in t["data"]:
    if(x["text"] not in r):
        r.append(x["text"])
        print(i,x["text"])
        i += 1
