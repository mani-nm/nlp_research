import tweepy, json
from difflib import SequenceMatcher


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def similar(self, a, b):
        for i in a:
            for j in b:
                if SequenceMatcher(None, j, i).ratio() >=0.6 and abs(len(i)-len(j))<3:
                    return True
        return False

    def on_status(self, status):
        #tweets = open("tweets.txt", 'w')
        #tweets.write(status.text)
        #tweets.close()
        #print(status.text)
        pass

    def on_data(self, data):
        f = open('drugList.csv', 'r')
        drugs = []
        for i in f:
            i = i.lower().rstrip().lstrip()
            drugs.append(i)
        f.close()

        decoded = json.loads(data)
        text = '@@@'
        if 'text' in decoded:
            text = decoded['text'].lower()
            word_list = text.split()
        #followers_count = decoded['followers_count']
        lang = 'en'
        if 'lang' in decoded:
            lang = decoded['lang']
        if 'rt @' not in text and lang == 'en' and self.similar(word_list, drugs) and ':battle id' not in text:
            print(text)
            with open('fetched_tweets1.txt', 'a', encoding="utf-8") as tf:
                tf.write(data)
        return True

    def on_error(self, status_code):
        #print(status_code)
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

    def on_exception(self, exception):
        """Called when an unhandled exception occurs."""
        return


# Consumer keys and access tokens, used for OAuth
consumer_key = 'auUCtC6PTUW3LQ9XiVUXEXnYS'
consumer_secret = 'sxZEJ5a1AKhRxUqBIY6KQzbtN26wgUBMS2HLQJdoW3wfwaZHBE'
access_token = '433511030-gSROLIFN0G838Pdw51cLanRYFikC9vcIxXAgM5D4'
access_token_secret = 'onw6tH87OsvDrdKN9J7xiO8k14gdkJRt9hcEvCupeNl7e'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# listener = StdOutListener()
# stream = tweepy.Stream(auth, listener)
# stream.filter(track=)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, myStreamListener)
drugs = []
f = open('drugList.csv', 'r')
for i in f:
    i = i.lower().rstrip().lstrip()
    drugs.append(i)
f.close()

myStream.filter(track=drugs,async=True)
