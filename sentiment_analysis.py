import config
import tweepy
from textblob import TextBlob

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

query = input("Please enter a keyword to perform a sentiment analysis on: ")

public_tweets = api.search(str(query))
neutral = 0
positive = 0
negative = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)

    """Aggregate all the noun phrases within the tweets"""
    print(analysis.noun_phrases)

    """Calculate the polarity for the collection of tweets containing the query"""
    if analysis.sentiment.polarity > 0:
        positive=+1
    elif analysis.sentiment.polarity < 0:
        negative+=1
    else:
        neutral+=1


totalPolarity = positive + negative + neutral
print('Postive:', (positive/totalPolarity)*100)
print('Negative:',(negative/totalPolarity)*100)
print('Neutral:', (neutral/totalPolarity)*100)
