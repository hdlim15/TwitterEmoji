# Hyuckin David Lim
# sort.py
#
# Organize tweets based on which emojis they contain


import json
import preprocess as pp
import constants as c


emoji_list = c.emoji_list

organized_tweets = {}
for emoji in emoji_list:
	organized_tweets[emoji] = []

found_emojis = set()

with open("tweet_dataset.json", "r") as tweet_file:
	tweet_dataset = json.loads(tweet_file.read())


for tweet in tweet_dataset:
	for emoji in emoji_list:
		if emoji in tweet:
			found_emojis.add(emoji)

	tweet = pp.preprocess_all(tweet)
	for emoji in found_emojis:
		organized_tweets[emoji].append(tweet)
	found_emojis = set()
	

for emoji in emoji_list:
	organized_tweets[emoji] = list(set(organized_tweets[emoji]))


jsonified = json.dumps(organized_tweets, indent=4)
with open("sorted.json", "w") as sorted:
	sorted.write(jsonified)