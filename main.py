import datetime
from flask import Flask
import politician as p
import tweepy
import requests
from bs4 import BeautifulSoup
import tweet_sentiment_analyzer as tsa
import numpy
import plot_analytics as graph_data
import senators as sen
import json
import sys
import twitterkeys as tk


senate_members = []
house_members = []


def scrape_senate_handles():
    """
    :return: updates the global "senate_members" to include a list of Politician Objects.
    """

    # Placeholder code below for scraping an oudated site with Senators twitter information

    # URL = "https://www.socialseer.com/resources/us-senator-twitter-accounts/"
    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, "html.parser")
    # table = soup.find('table')

    # rows = table.find_all('tr')
    # for row in rows[1:]:
    #     cols = row.find_all('td')
    #     cols = [ele.text.strip() for ele in cols]
    #     senate_members.append(cols[2])

    senators = sen.generate_senators()
    for sen in senators:
        s = p.Politician(sen[0], sen[1], sen[2], sen[3], sen[4])
        senate_members.append(s)




def scrape_house_handles():
    """
    :return: updates the global "house_members" to include a list of Politician Objects
    """
    congress_url = "https://pressgallery.house.gov/member-data/members-official-twitter-handles"
    house_page = requests.get(congress_url)
    congress_soup = BeautifulSoup(house_page.content, "html.parser")
    table = congress_soup.find('table')
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        pol = p.Politician(cols[0], cols[1], (cols[2])[1:], cols[3], cols[4], 1)
        house_members.append(pol)

    return house_members


auth = tweepy.OAuthHandler(tk.genkeys['consumer_key'], tk.genkeys['consumer_secret'])
auth.set_access_token(tk.genkeys['access_token_key'], tk.genkeys['access_token_secret'])

api = tweepy.API(auth)

warHits = ["Russia", "Ukraine", "War "]


def containsWord(tweet, listofwords):
    """
    :param tweet: a tweet in String format
    :param listofwords: a list of Strings to check if they are in the Tweet
    :return: returns True if the tweet contains a word in the given list of words. Returns False otherwise. 
    """
    contains = False
    for word in listofwords:
        if word in tweet:
            contains = True
            break

    return contains



def plotTweetsPerDay(dayRange, twitterusers):
    """
    :param dayRange: range of UTC dates passed as a list ["04-02-2022", "04-21-2022"]
    :param twitterusers: list of users twitter handles ["jaymack1", "asiel", "portleyashley"]
    :return: a dict in the date:tweets format, where "tweets" is a list of all the tweets the given users posted on that date 
    """
    daytotweets = {}
    recordTweets = ["placeholder", 0]
    lowestTweets = ["placeholder", 100]
    for day in dayRange:
        daytotweets.update({day: 0})
    for user in twitterusers:
        max = 0
        min = 0
        try:
            senUserTimeline = api.user_timeline(screen_name=user)
        except:
            print("User Account Deleted")
        for tweet in senUserTimeline:
            for day in dayRange:
                if day in str(tweet.created_at):
                    daytotweets[day] += 1
                    max += 1
                    min += 1
                else:
                    continue
        if max > recordTweets[1]:
            recordTweets = [user, max]
        if min < lowestTweets[1]:
            lowestTweets = [user, min]


    return daytotweets


def day_range(d_range):
    """
    :param d_range: a list of two days, start and end, in string format
    :return: returns a list of days in string format between the given range, inclusive.
    """
    range_temp = []
    start = datetime.datetime.strptime(d_range[0], "%Y-%m-%d")
    end = datetime.datetime.strptime(d_range[1], "%Y-%m-%d")
    dates_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days + 1)]
    for date in dates_generated:
        range_temp.append(date.strftime("%Y-%m-%d"))
    return range_temp


def large_data(twitter_handles, day_range_list):
    """
    :param twitter_handles: list of twitter handles as strings
    :param day_range_list: range of days to get tweets for in [start_date, end_date] format
    :return: a list of tweets
    """
    tweets_nltk = []
    results = {}
    day_range_temp = day_range(day_range_list)
    for day in day_range_temp:
        results.update({day: 0})

    # results - dictionary of Tweets with days as the keys and lists of Tweets as the vals e.g. {"2022-04-17":[Tweet1, Tweet2, Tweet3]}

    for pol in twitter_handles:
        individual_results = pol.tweets_on_days(day_range_list, api)
        for k in individual_results:
            results[k] += len(individual_results[k])
            for tweet in individual_results[k]:
                tweets_nltk.append(tweet._json['full_text'])

    return tweets_nltk


def filter_by_party(members, desired_party):
    """
    :param members: a list of Politicians to filter
    :param desired_party: democrat or republican, passed as "Democrat" or "Republican"
    :return: a filtered list of democrats or republicans
    """
    if desired_party == "Democrat":
        return [p for p in members if p.party == "D"]
    if desired_party == "Republican":
        return [p for p in members if p.party == "R"]

def filter_by_state(members, desired_states):
    """
    :param members: a list of politicians to filter
    :param desired_states: a list of states to filter by, e.g. ["CA", "NY", "OR"]
    :return: a filtered list of congress members representing the given states
    """
    state_members = []
    for p in members:
        if p.district[0:2] in desired_states:
            state_members.append(p)
    return state_members

#Flask declaration
app = Flask(__name__)



@app.route("/members")
def members():
    """
    :return: the default data for the Political Tweet Tool.  
    """
    running_democrat_average = []
    running_republican_average = []

    all_house_members = scrape_house_handles()
    democrats = filter_by_party(all_house_members, "Democrat")
    republicans = filter_by_party(all_house_members, "Republican")

    for d in democrats[0:3]:
        running_democrat_average.append(d.get_average_sentiment(api))
    for r in republicans[0:3]:
        running_republican_average.append(r.get_average_sentiment(api))
    
    democrat_average = numpy.mean(running_democrat_average)
    republican_average = numpy.mean(running_republican_average)

    return {"labels" : ["Democrats", "Republicans"], "averages" : [democrat_average, republican_average], "state" : [""]}
    

@app.route("/default_data_set")
def default_data_set():
    return {"labels": ["big", "small"], "averages": [1, 2]}



@app.route('/line_graph_data<data>')
def line_graph_data(data):
    """
    :param data: a JSON list of desired filters to be applied to the line graph
    :return: a dict in the number_of_followers:average_sentiment format 
    """
    conv = json.loads(data)
    desired_party = conv[0]
    desired_state = [conv[1]]
    desired_house = conv[2]
    all_house_members = scrape_house_handles()
    follower_number_to_sentiment = {}


    if desired_state[0] != "":
        all_house_members = filter_by_state(all_house_members, desired_state[0])
        

    if desired_party == "Both":
        for m in all_house_members[0:10]:
            follower_number_to_sentiment[m.get_follower_count(api)] = m.get_average_sentiment(api)
        jsonconv = json.dumps(follower_number_to_sentiment)
        return jsonconv

    all_house_members = filter_by_party(all_house_members, desired_party)

    for m in all_house_members[0:10]:
        follower_number_to_sentiment[m.get_follower_count(api)] = m.get_average_sentiment(api)

    jsonconv = json.dumps(follower_number_to_sentiment)
    return jsonconv



@app.route('/select_data<data>')
def select_data(data):
    """
    :param data: a JSON list of desired filters to be applied to the bar graph
    :return: a dict in the label:data format (String:list of Strings/Ints)
    """
    conv = json.loads(data)
    print(conv, file=sys.stderr)
    desired_party = conv[0]
    desired_state = [conv[1]]
    desired_house = conv[2]
    all_house_members = scrape_house_handles()
    running_party_average = []
    running_democrat_average = []
    running_republican_average = []
    follower_numbers = []
    
    if desired_state[0] != "":
        all_house_members = filter_by_state(all_house_members, desired_state[0])
    

    if desired_party == 'Both':
        democrats = filter_by_party(all_house_members, "Democrat")
        for d in democrats:
            running_democrat_average.append(d.get_average_sentiment(api))

        republicans = filter_by_party(all_house_members, "Republican")
        for r in republicans:
            running_republican_average.append(r.get_average_sentiment(api))
    
        democrat_average = numpy.mean(running_democrat_average)
        republican_average = numpy.mean(running_republican_average)
        return {"labels" : ["Democrats", "Republicans"], "averages" : [democrat_average, republican_average], "state" : [desired_state]}
    
    party_members = filter_by_party(all_house_members, desired_party)

    for p in party_members:
        running_party_average.append(p.get_average_sentiment(api))
        follower_numbers.append(p.get_follower_count(api))

    party_average = numpy.mean(running_party_average)

    return {"labels" : [desired_party+"s"], "averages" : [party_average], "state": [desired_state]}



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
    