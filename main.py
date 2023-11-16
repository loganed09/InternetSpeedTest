from twitter_bot import InternetSpeedTwitterBot
import os

PROMISED_DOWN = 150
PROMISED_UP = 50

TWITTER_EMAIL  = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")

bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)


bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_USERNAME, TWITTER_PASSWORD)