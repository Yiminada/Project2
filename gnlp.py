
from google.cloud import language
import pandas as pd
client = language.LanguageServiceClient.from_service_account_json("path/file")


columns = ['Text','Sentiment Score','Sentiment Magnitude']
data = []
pd.set_option('display.max_rows', None)
f = open("testfile.txt", "r")
while True:
    text = f.readline()
    if not text:
        break
    document = language.Document(content = text,type = language.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request = {"document": document}).document_sentiment
    data.append([text,sentiment.score,sentiment.magnitude])
df = pd.DataFrame(data,columns=columns)
print(df)
f.close()

