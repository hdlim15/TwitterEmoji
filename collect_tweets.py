import tweepy
import json
import time
import constants as c

# global variables
tweet_json = []
tweet_count = 0
current_label = ""
filler_tweets = 0

class StreamListener(tweepy.StreamListener):

	def on_status(self, status):
		if status.lang != "en": # only english
			return
		try:	# ignore retweets
			if status.retweeted_status:
				return
		except:
			pass

		global tweet_count
		global tweet_json

		text = status.text
		# print(tweet_count)
		# print(text)
		tweet_count += 1
		tweet_json.append(text)

		if (tweet_count % 100 == 0):
			print(tweet_count)
			x = json.dumps(tweet_json, indent=4)
			aa = open("collection.json", "w")
			aa.write(x)
			aa.close()

		# if (tweet_count == 80):
		# global filler_tweets
		# if (tweet_count == filler_tweets):
		# 	return False

	def on_error(self, status_code):
		if status_code == 420:
			# Returning False in on_data disconnects the stream
			return False


def stream(searchItems):
	consumer_key="QCjnoDCt1C84pUEq0X1YQkA6c"
	consumer_secret="tnvuyzzT4avQNvBlCw6tgXRsw8PTJnm6n88LaHUQJd3b8Rd8ZW"
	oauth_token="798995709638938625-s44zhMvpPbtzwNb0Ie2FjDKxiTuoy0U"
	oauth_token_secret="lsrnyPMLZt6p731O6gFrR63mUAog9XHC8OOnGhqa7qp20"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(oauth_token, oauth_token_secret)
	api = tweepy.API(auth)

	streamListener = StreamListener()
	stream = tweepy.Stream(auth = api.auth, listener=streamListener)
	stream.filter(track=searchItems)



emoji_list = c.emoji_list
label = c.keys
# for l in label:
# 	tweet_json[l] = []


# for i in range(0, 80):
# 	current_label = label[i]
# 	while (tweet_count < filler_tweets):
		# try:
		# 	stream(emoji_list[i])
		# except:
		# 	pass
# 	x = json.dumps(tweet_json, indent=4)
# 	a = open("tweet_dataset.txt", "w")
# 	a.write(x)
# 	a.close()
# 	tweet_count = 0
# 	print("\n\nFinished: " + label[i] + "\n\n")

# length_array = [100, 100, 100, 99, 100, 100, 100, 99, 100, 99, 96, 100, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 98, 98, 98, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 100, 100, 100, 99, 100, 100, 100, 100, 99, 100, 100, 100, 100, 100, 100, 100, 100, 99, 99, 99, 100, 100, 99, 99, 100, 100, 100, 100, 100, 100, 100, 99, 100, 100, 100, 98, 100, 100, 100, 94, 100]
# for i in range(0, 80):
# 	filler_tweets = 100 - length_array[i]
# 	current_label = label[i]
# 	while (tweet_count < filler_tweets):
# 		try:
# 			stream(emoji_list[i])
# 		except:
# 			pass
# 	x = json.dumps(tweet_json, indent=4)
# 	a = open("tweet_dataset.txt", "w")
# 	a.write(x)
# 	a.close()
# 	tweet_count = 0
# 	print("\n\nFinished: " + label[i] + "\n\n")
with open("collection.json","r") as trtr:
	emoji_list = json.loads(trtr.read())
print(emoji_list)
while(True):
	try:
		stream(emoji_list)
	except:
		print("Failure")



