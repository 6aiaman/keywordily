import tweepy
import csv
import pandas as pd
import numpy


def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet 
    in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet 
    in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet 
    in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet 
    in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet 
    in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet 
    in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet 
    in tweets]

    return DataSet

def twitter_feed(user_query):
	consumer_key = "BIj9uMTrObsmj8cPvgbllw7I2"
	consumer_secret = "0i5EgSUs6NiGxwRcxLoL0GtoagcMsWnurUPcS8Oo4GZEoaISFR"
	access_token = "247837876-M3tU7S7QAi6f6n8AFogt52MhYNZSnAiONIhtBcZS"
	access_token_secret = "T8V1Ni5ass59TaM0bTNmcbbl4m6xTw1Wl0j3cRMAgzoV7"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	results = []
	for tweet in tweepy.Cursor(api.search, q=user_query, result_type='popular', lang='en').items(100):
	    results.append(tweet)

	#Pass the tweets list to the above function to create a DataFrame
	# twitter_news_df = toDataFrame(results)
	# return twitter_news_df
	
	return results
# a = twitter_feed('arsenal')
# a.to_csv("twitter_feed.csv", encoding='utf-8', index=False)

# print a



