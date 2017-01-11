# arr = ["\U0001f64f", "\U0001f64f\U0001f3fb", "\U0001f64f\U0001f3fc", "\U0001f64f\U0001f3fd", "\U0001f64f\U0001f3fe", "\U0001f64f\U0001f3ff"]

# # print("\U0001f64f" in arr)

# for a in arr:
# # 	a = a[0]
# 	print(a)
# # print(arr)

# colored_emojis = ["\U0001F645","\U0001F646","\U0001F647","\U0001F64B","\U0001F64C","\U0001F64D","\U0001F64E","\U0001F64F"]
# colors = ["\U0001f3fb","\U0001f3fc","\U0001f3fd","\U0001f3fe","\U0001f3ff"]
# for b in colored_emojis:
# 	for c in colors:
# 		print(b + c)


# x=[]

import constants as c
import json

# # hyuckin = open("test3.json", "r")
# # data = json.loads(hyuckin.read())
# # hyuckin.close()

# for a in ["0","1","2","3","4"]:
# 	for b in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
# 		x.append(a + b)

# for i in [66,71,72,73,76,77,78,79]:
# 	print(x[i])

emoji_list = c.emoji_list
new_set = []


# with open("tweet_dataset2.json", "r") as tweet_file:
# 	tweet_dataset = json.loads(tweet_file.read())
# for tweet in tweet_dataset:
# 	for emoji in emoji_list:
# 		if emoji in tweet:
# 			new_set.append(tweet)
# 			break

# with open("100each.json", "r") as tweet_file:
# 	tweet_dataset = json.loads(tweet_file.read())
# for key in tweet_dataset:
# 	for tweet in tweet_dataset[key]:
# 		for emoji in emoji_list:
# 			if emoji in tweet:
# 				new_set.append(tweet)
# 				break

# tweets_with_emojis = json.dumps(new_set, indent=4)
# with open("tweet_dataset.json", "w") as tweet_file:
# 	tweet_file.write(tweets_with_emojis)


shortList = []

with open("sorted.json", "r") as tweet_file:
	tweet_dataset = json.loads(tweet_file.read())
ten = 0
five = 0
one = 0
for x in emoji_list:
	lala = tweet_dataset[x]
	if len(lala) <5000:
		shortList.append(x)
		ten += 1
	if len(lala) > 5000:
		five += 1
	if len(lala) > 1000:
		one += 1
print(ten)
print(five)
print(one)

# with open("collection.json", "w") as afdsf:
# 	afdsf.write(json.dumps(shortList))




