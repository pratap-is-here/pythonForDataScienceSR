#twitter sentiment analyser

import tweepy
from textblob import TextBlob

consumer_key='5htVpJaPfItdQcak6UkEkWtLT'
consumer_secret='HYTm5RTpmkJY92roRzXyAddjrsDUT4fF8Ih769byiQI4OrIqoO'

access_token='1002108329051570176-UsHlRo0OenI0ghf1FUr9EjdD6PtYWv'
access_token_secret='o2haZ3t5th7fbKThnTDQvXq1OnSKQypUzpW2MuoYKnIFg'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Modi')

for tweet in public_tweets:
    print (tweet.text.encode("utf-8"))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
