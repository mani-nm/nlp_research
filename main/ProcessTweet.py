import json
import pandas as pd

with open('fetched_tweets1.txt') as json_data:
    d = json.load(json_data)

for i in d:
    print (i)
    break
#df = pd.read_json("fetched_tweets1.txt", orient='split')
#df.head(5)




