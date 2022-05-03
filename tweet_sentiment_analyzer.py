import main as m
import politician as p
import re
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def clean_tweets(tweets):
    """
    :param tweets: a list of tweets (str)
    :return: a list of tweets excluding RTs, links, and new lines
    """
    new_tweets = []
    for tweet in tweets:
        if tweet[0:2] != "RT":
            tweet = re.sub(r'https\S+', '', tweet)
            tweet = re.sub(r'\n', ' ', tweet)
            new_tweets.append(tweet)
    return new_tweets


def analyze_tweets_sentiments(tweets):
    """
    :param tweets: list of tweets to be sentiment-analyzed
    :return: 
    """
    output = []
    for tweet in tweets:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(tweet)
        for k in sorted(ss):
            output.append(ss)
            #print('{0}: {1}, '.format(k, ss[k]), end='')
    return output

