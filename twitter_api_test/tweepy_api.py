import tweepy
import pandas as pd

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

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

hashtags = 'any keyword or hashtag'
count = 0

public_tweets = api.search_tweets(q = hashtags,count = count,tweet_mode = 'extend')
columns = ['Time','User','Tweet']
data = []
pd.set_option('display.max_rows', None)
for tweet in public_tweets:
    data.append([tweet.created_at,tweet.user.screen_name,tweet.text])
df = pd.DataFrame(data,columns=columns)
print(df)

