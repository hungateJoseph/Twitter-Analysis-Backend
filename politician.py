import main as m
import tweet_sentiment_analyzer as tsa
import numpy


class Politician:
    def __init__(self, first_name, last_name, twitter_handle, district, party, follower_count):
        self.first_name = first_name
        self.last_name = last_name
        self.twitter_handle = twitter_handle
        self.district = district
        self.party = party
        self.average_sentiment_rating = 0.0
        self.follower_count = follower_count

    def __repr__(self):
        return "printed instance"

    def __str__(self):
        return ("First name: " + self.first_name + " Last name: " + self.last_name + " twitter_handle: " +
                self.twitter_handle + " district: " + self.district + " party: " + self.party + "number of followers: " + str(self.follower_count))

    def tweets_on_days(self, days_list, api, date_range=True):
        """
        :param days_list: list of specific days in the "YYYY-MM-DD" format or a range of dates between two days
        :param api: a reference to the Tweepy authentication api
        :param date_range: indicates whether the given list of days is a range or specific dates. Defaults to True
        :return: a dictionary of day:Tweets
        """
        day_to_tweets = {}
        if date_range:
            expanded_days = m.day_range(days_list)
            days_list = expanded_days

        for day in days_list:
            day_to_tweets.update({day: []})
        try:
            pol_timeline = api.user_timeline(screen_name=self.twitter_handle, tweet_mode='extended')
            for tweet in pol_timeline:
                if str(tweet.created_at.date()) in days_list:
                    (day_to_tweets[str(tweet.created_at.date())]).append(tweet)
        except:
            print("Unable to retrieve user timeline: " + self.twitter_handle)

        return day_to_tweets

    def get_sentiment_ratings(self, api):
        """
        :return: a list of sentiment ratings for all the user's tweets in their past 20 statuses (Tweedy api
        only allows a max of 20 statuses/call)
        """
        tweet_list = []
        try:
            self_timeline = api.user_timeline(screen_name=self.twitter_handle, tweet_mode='extended')
            for tweet in self_timeline:
                tweet_list.append(tweet._json['full_text'])
            cleaned_tweets = tsa.clean_tweets(tweet_list)
            return tsa.analyze_tweets_sentiments(cleaned_tweets)
        except:
            print("Unable to retrieve user timeline: " + self.twitter_handle)
            return []

    def get_average_sentiment(self, api):
        """
        :param api: tweedy api reference
        :return: the politician's average tweet sentiment for their past 20 statuses
        """
        compound_scores = []
        ratings = self.get_sentiment_ratings(api)
        if not ratings:
            return 0.0
        for score in ratings:
            compound_scores.append(score['compound'])
        return numpy.mean(compound_scores)

    def get_follower_count(self, api):
        """
        :param api: tweedy api reference
        :return: the number of Twitter followers the given politician has.
        """
        try:
            followers = api.get_user(screen_name=self.twitter_handle)
            total = followers.followers_count
            return total
        except:
            print("Unable to retrieve user timeline: " + self.twitter_handle)