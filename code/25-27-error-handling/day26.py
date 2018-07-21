# https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library

from __future__ import absolute_import, print_function
from datetime import datetime, timedelta
from json import loads
import tweepy
import requests
from time import sleep


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# my_tweet = input("What would you like to tweet")

ignore_list = ["_30days30sites", "100_DaysOfCode", "100_DaysOfCode_", "100DaysOfCode_", "_100DaysOfCode", "Evil_1T",
               "lancetay", "DaysofcodeNg", "rogue_corq", "muthiimm", "GitLit000", "gadgetgirlcodes", "TheDevelBot",
               "python_octopus"]


def retweet_like_follow(hashtag):
    """Retweet, Like, and Follow users based off hashtag"""
    for tweet in tweepy.Cursor(api.search, q=hashtag).items():
        try:
            if tweet.user.screen_name in ignore_list:
                continue
            # Add \n escape character to print() to organize tweets
            print('\nTweet by: @' + tweet.user.screen_name)

            # Retweet tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet')

            # Favorite the tweet
            tweet.favorite()
            print('Favorited the tweet')

            if not tweet.user.following:
                # Don't forget to indent
                tweet.user.follow()
                print('Followed the user')

            sleep(60)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def follow_followers():
    """Follow everyone who is following you"""
    user = api.me()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print("Followed {} that is following ".format(follower.follow()) + user.name)


# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)


if __name__ == '__main__':

    # api.update_status(my_tweet)
    # follow_followers()
    retweet_like_follow("100DaysOfCode")
    # print(my_tweet)
