# Hyuckin David Lim
# VADER.py
#
# Credit for the VADER model goes to:
# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
# Sentiment Analysis of Social Media Text. Eighth International Conference on
# Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
# http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf
#
# Using VADER (Valence Aware Dictionary for sEntiment Reasoning) 
# to perform an initial analysis of the tweets


import json
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import preprocess as pp
import constants as c


with open("sorted.json", "r") as tweet_file:
	tweet_dataset = json.loads(tweet_file.read())


vader = SentimentIntensityAnalyzer()

# contains the sentiment for each emoji
sentiment_dict = {}

neg = 0
neu = 0
pos = 0
compound = 0

for key in c.emoji_list:
	sentiment_dict[key] = 0 # average sentiment starts at 0
	count = 0				# number of tweets
	for tweet in tweet_dataset[key]:
		tweet = pp.remove_emojis(tweet)
		values = vader.polarity_scores(tweet)
		compound = values["compound"]
		pos = values["pos"]
		neg = values["neg"]
		neu = values["neu"]

		sentiment_dict[key] += compound
		count += 1

	# Average sentiment per tweet for a specific emoji
	sentiment_dict[key] /= count
	print(count)

# Sort by sentiment value and then print
sentiment_dict = sorted(sentiment_dict.items(), key=lambda x:x[1])
for entry in sentiment_dict:
	print(entry)

results = json.dumps(sentiment_dict, indent=4)
with open("VADER_results.json", "w") as result_file:
	result_file.write(results)

