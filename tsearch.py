import tweepy
from textblob import TextBlob

consumer_key = 	'6Kewm70tkxW6R5fKoeVNsO2Mp'
consumer_secret = 'PsVHreJthpYAgR24TvF65FspFPMLrSSFnqtD8ONZ22r1dccBQt'

access_token = '750956656050180097-c5qKv5Y6A27PifGymcKmlTjcBCzcs28'
access_token_secret = 'Bwyvlmgy4CnZpbMqSzlsPdiSKIlV6OxcplC4pQLBV9YU7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search() 

for tweet in public_tweets:
	print(tweet.text)
	
