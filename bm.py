import botometer

rapidapi_key = "XXXXXX"
twitter_app_auth = {
    'consumer_key': 'XXXXXX',
    'consumer_secret': 'XXXXXX',
    'access_token': 'XXXXXX',
    'access_token_secret': 'XXXXXX',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)
"""
result = bom.check_account('screen name or user id')
print(result)
"""
f = open("result.txt", "w+")
accounts = ['screen name','user id']
for result in bom.check_accounts_in(accounts):
  s = str(result) + "\n"
  f.write(s)
f.close()
