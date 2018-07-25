# https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
# https://dototot.com/reply-tweets-python-tweepy-twitter-bot/
# https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets

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

# twts = api.search()

ignore_list = ["_30days30sites", "100_DaysOfCode", "100_DaysOfCode_", "100DaysOfCode_", "_100DaysOfCode", "Evil_1T",
               "lancetay", "DaysofcodeNg", "rogue_corq", "muthiimm", "GitLit000", "gadgetgirlcodes", "TheDevelBot",
               "python_octopus", "AaronCuddeback", "AlexShiresRoth", "WomenWhoCode_", "newtonmunene_yg"]


def retweet_like_follow(hashtag):
    """Retweet, Like, and Follow users based off hashtag"""
    for tweet in tweepy.Cursor(api.search, q=hashtag + " -filter:retweets", tweet_mode='extended').items():
        try:
            # ignore users on the ignore list
            if tweet.user.screen_name in ignore_list:
                continue
            # Print user and tweet
            print('\nTweet by: @' + tweet.user.screen_name)
            # print("\n" + str(tweet))
            # print(type(tweet))
            print(tweet.full_text)
            # print(tweet.extended_tweet)
            sleep(1)

            # Retweet tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet')
            sleep(2)

            # Favorite the tweet
            tweet.favorite()
            print('Favorited the tweet')
            sleep(1)

            # Follow the user if you aren't already
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

            sleep(15)
        except ConnectionResetError:
            break
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
