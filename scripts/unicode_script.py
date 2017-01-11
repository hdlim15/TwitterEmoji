hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

with open("emoji_unicode.txt", "w") as emojis:
	emojis.write("[")
	for x in ["0","1","2","3","4"]:
		for y in hex:
			emojis.write("\"\\U0001F6" + x + y + "\",")
		# emojis.write("\n")
	emojis.write("]")
	emojis.close()