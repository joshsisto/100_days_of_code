# https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
# https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/

from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json




class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(type(data))
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        print(username)
        print(tweet)
        # username.favorite()
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(track=['100DaysOfCode', "Bitcoin"], languages=["en"])
    stream.api(tweet_mode='extended')
