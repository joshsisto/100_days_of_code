# https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607
# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
# https://dototot.com/reply-tweets-python-tweepy-twitter-bot/
# https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets

from __future__ import absolute_import, print_function
import tweepy
from time import sleep
import logbook
from credentials import *

app_log = logbook.Logger('App')
logbook.set_datetime_format("local")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# my_tweet = input("What would you like to tweet")

# twts = api.search()

ignore_list = ["_30days30sites", "100_DaysOfCode", "100_DaysOfCode_", "100DaysOfCode_", "_100DaysOfCode", "Evil_1T",
               "lancetay", "DaysofcodeNg", "rogue_corq", "muthiimm", "GitLit000", "gadgetgirlcodes", "TheDevelBot",
               "python_octopus", "AaronCuddeback", "AlexShiresRoth", "WomenWhoCode_", "newtonmunene_yg", "RanitSarker"]


def retweet_like_follow(hashtag):
    """Retweet, Like, and Follow users based off hashtag"""
    for tweet in tweepy.Cursor(api.search, q=hashtag + " -filter:retweets", tweet_mode='extended', language="en").items():
        try:
            # ignore users on the ignore list
            if tweet.user.screen_name in ignore_list:
                app_log.trace("Skipping {} because they are on the ignore list.".format(tweet.user.screen_name))
                continue
            # Print user and tweet
            print('\nTweet by: @' + tweet.user.screen_name)
            print(tweet.full_text)
            app_log.trace("Printed user and tweet {}".format(tweet.user.screen_name))
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

            sleep(90)
        except ConnectionResetError:
            msg = "You've been disconnected"
            print("ERROR: " + msg)
            app_log.warn(msg)
            break
        except tweepy.TweepError as e:
            msg = "This is a Tweepy Error: {}".format(e)
            print(msg)
            app_log.warn(msg)
        except StopIteration:
            msg = "I don't even know what StopIteration means"
            print("ERROR: {}".format(msg))
            break
        except KeyboardInterrupt:
            msg = "Keyboard Interrupt"
            print("ERROR: {}".format(msg))
        except Exception as x:
            msg = "oh that didn't work!: {}".format(x)
            print(msg)
            app_log.exception(x)


def follow_followers():
    """Follow everyone who is following you"""
    user = api.me()
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print("Followed {} that is following ".format(follower.follow()) + user.name)


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)


if __name__ == '__main__':

    # api.update_status(my_tweet)
    # follow_followers()
    init_logging('twitter_bot.log')
    retweet_like_follow("100DaysOfCode")
    # print(my_tweet)
