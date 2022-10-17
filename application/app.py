import tweepy
from google.cloud import language 
import pandas as pd

twitter = {
    "api_key" : "j9rqAEqJsyWAnRFhfAqYAP5eB",
    "api_key_secret" : "kAKLcrSgtGxtCtQvBHvfRrI7ujH1jLj3MJjzAXoM6vrMcL4Njd",
    "access_token" : "1579705373300228096-jeULgth3NO8kOs8T3RVA8K3661yNdT",
    "access_token_secret" : "xmZiTpBFRB8MTJOZywjz0WXZ1yzTRjrs66MGJmxjslHJO"
}
api_key = twitter["api_key"]
api_key_secret  = twitter["api_key_secret"]
access_token = twitter["access_token"]
access_token_secret = twitter["access_token_secret"]
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
count = 30
client = language.LanguageServiceClient.from_service_account_json("/Users/chenxiluo/project2/googlenlp/ec601-project2-365403-218d0a9cdabb.json")
hashtags = 'Boston University'
public_tweets = api.search_tweets(q = hashtags,count = count,tweet_mode = 'extend')
columns = ['Time','User','Tweet','Score','magnitude']
pd.set_option('display.max_columns', None)
data = []
sums = 0
summ = 0
avgs = 0
aygm = 0
#ns = 0
#nm = 0
for tweet in public_tweets:
    document = language.Document(content = tweet.text,type = language.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request = {"document": document}).document_sentiment
    data.append([tweet.created_at,tweet.user.screen_name,tweet.text,sentiment.score,sentiment.magnitude])
    sums += sentiment.score
    #ns += 1
    summ += sentiment.magnitude
   # nm += 1
df = pd.DataFrame(data,columns=columns)
avgs = float(sums) / count
avgm = float(summ) / count
f = open("result.txt", "w+")
f.write(df.to_string())
s = "\n" + str("Average of sentiment score: ") + str(avgs) + "\n"
ss = str("Average of sentiment magnitude: ") + str(avgm) + "\n"
f.write(df.to_string())
f.write(s)
f.write(ss)
f.close()

