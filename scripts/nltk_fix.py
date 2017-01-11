# Natural Language ToolKit has a Tweet Tokenizer that is supposed to remove Twitter handles.
# Their regex is wildly incorrect, so I have written a new and correct regex.
# These test cases represent all the different edge cases I could find.

# test_re contains tests I used to test my new regex
# test_remove_handle contains unit tests that I wrote for nltk after they accepted my regex


import re
from nltk.tokenize import TweetTokenizer

# Tests a re pattern against several tweets and sees how accurately it removes twitter handles
def test_re(pattern):
	# An array of tweets to test
	test_array = [
		# Simple example. Handles with just numbers should be allowed
		"@twitter hello @twi_tter_. hi @12345 @123news",
		# Handles are allowed to follow any of the following characters
		"@n`@n~@n(@n)@n-@n=@n+@n\\@n|@n[@n]@n{@n}@n;@n:@n'@n\"@n/@n?@n.@n,@n<@n>@n @n\n@n ñ@n.ü@n.ç@n.",
		# Handles are NOT allowed to follow any of the following characters
		"a@n j@n z@n A@n L@n Z@n 1@n 4@n 7@n 9@n 0@n _@n !@n @@n #@n $@n %@n &@n *@n",
		# Handles are allowed to precede the following characters
		"@n!a @n#a @n$a @n%a @n&a @n*a",
		# Tests interactions with special symbols and multiple @
		"@n!@n @n#@n @n$@n @n%@n @n&@n @n*@n @n@n @@n @n@@n @n_@n @n7@n @nj@n",
		# Tests that handles can have a max length of 20 
		"@abcdefghijklmnopqrstuvwxyz @abcdefghijklmnopqrst1234 @abcdefghijklmnopqrst_ @abcdefghijklmnopqrstendofhandle",
		# Edge case where an @ comes directly after a long handle
		"@abcdefghijklmnopqrstu@abcde @abcdefghijklmnopqrst@abcde @abcdefghijklmnopqrst_@abcde @abcdefghijklmnopqrst5@abcde"
	]

	# An array of the above tweets with the handles removed, as experimented on twitter
	solution_array = [
		" hello . hi  ",
		"`~()-=+\\|[]{};:'\"/?.,<> \n ñ.ü.ç.",
		"a@n j@n z@n A@n L@n Z@n 1@n 4@n 7@n 9@n 0@n _@n !@n @@n #@n $@n %@n &@n *@n",
		"!a #a $a %a &a *a",
		"!@n #@n $@n %@n &@n *@n @n@n @@n @n@@n @n_@n @n7@n @nj@n",
		"uvwxyz 1234 _ endofhandle",
		"u@abcde @abcdefghijklmnopqrst@abcde _@abcde 5@abcde"
	]

	passed_all_tests = True
	failed_tests = "Failed tests: "

	for i in range(0, len(test_array)):
		test = test_array[i]
		solution = solution_array[i]

		removed = pattern.sub("", test)
		if removed == solution:
			print("Passed test " + str(i))
		else:
			passed_all_tests = False
			failed_tests += str(i) + ", "
			print("\nFailed test " + str(i))
			print("Your    Solution: " + removed)
			print("Correct Solution: " + solution)

	if passed_all_tests:
		print("All tests passed")
	else:
		print(failed_tests[:len(failed_tests)-2])


# Unit tests for NLTK
# https://github.com/nltk/nltk/blob/develop/nltk/test/unit/test_tokenize.py
def test_remove_handle(self):
    """
    Test remove_handle() from casual.py with specially crafted edge cases
    """

    tokenizer = TweetTokenizer(strip_handles=True)
    
    # Simple example. Handles with just numbers should be allowed
    test1 = "@twitter hello @twi_tter_. hi @12345 @123news"
    expected = ['hello', '.', 'hi']
    result = tokenizer.tokenize(test1)
    self.assertEqual(result, expected)
    
    # Handles are allowed to follow any of the following characters
    test2 = "@n`@n~@n(@n)@n-@n=@n+@n\\@n|@n[@n]@n{@n}@n;@n:@n'@n\"@n/@n?@n.@n,@n<@n>@n @n\n@n ñ@n.ü@n.ç@n."
    expected = ['`', '~', '(', ')', '-', '=', '+', '\\', '|', '[', ']', '{', '}', ';', ':', "'", '"', '/', '?', '.', ',', '<', '>', 'ñ', '.', 'ü', '.', 'ç', '.']
    result = tokenizer.tokenize(test2)
    self.assertEqual(result, expected)
    
    
    # Handles are NOT allowed to follow any of the following characters
    test3 = "a@n j@n z@n A@n L@n Z@n 1@n 4@n 7@n 9@n 0@n _@n !@n @@n #@n $@n %@n &@n *@n"
    expected = ['a', '@n', 'j', '@n', 'z', '@n', 'A', '@n', 'L', '@n', 'Z', '@n', '1', '@n', '4', '@n', '7', '@n', '9', '@n', '0', '@n', '_', '@n', '!', '@n', '@', '@n', '#', '@n', '$', '@n', '%', '@n', '&', '@n', '*', '@n']
    result = tokenizer.tokenize(test3)
    self.assertEqual(result, expected)
    
    
    # Handles are allowed to precede the following characters
    test4 = "@n!a @n#a @n$a @n%a @n&a @n*a"
    expected = ['!', 'a', '#', 'a', '$', 'a', '%', 'a', '&', 'a', '*', 'a']
    result = tokenizer.tokenize(test4)
    self.assertEqual(result, expected)
    
    
    # Tests interactions with special symbols and multiple @
    test5 = "@n!@n @n#@n @n$@n @n%@n @n&@n @n*@n @n@n @@n @n@@n @n_@n @n7@n @nj@n"
    expected = ['!', '@n', '#', '@n', '$', '@n', '%', '@n', '&', '@n', '*', '@n', '@n', '@n', '@', '@n', '@n', '@', '@n', '@n_', '@n', '@n7', '@n', '@nj', '@n']
    result = tokenizer.tokenize(test5)
    self.assertEqual(result, expected)
    
    
    # Tests that handles can have a max length of 20
    test6 = "@abcdefghijklmnopqrstuvwxyz @abcdefghijklmnopqrst1234 @abcdefghijklmnopqrst_ @abcdefghijklmnopqrstendofhandle"
    expected = ['uvwxyz', '1234', '_', 'endofhandle']
    result = tokenizer.tokenize(test6)
    self.assertEqual(result, expected)
    
    
    # Edge case where an @ comes directly after a long handle
    test7 = "@abcdefghijklmnopqrstu@abcde @abcdefghijklmnopqrst@abcde @abcdefghijklmnopqrst_@abcde @abcdefghijklmnopqrst5@abcde"
    expected = ['u', '@abcde', '@abcdefghijklmnopqrst', '@abcde', '_', '@abcde', '5', '@abcde']
    result = tokenizer.tokenize(test7)
    self.assertEqual(result, expected)


# Fails tests 0, 1, 3, 4, 5, 6
nltk_pattern = re.compile(r"(^|(?<=[^\w.-]))@[A-Za-z_]+\w+")
print("Current remove_handles re: ")
test_re(nltk_pattern)

print()

# Passes all tests
my_pattern = re.compile(r"(?<![A-Za-z0-9_!@#\$%&*])@((([A-Za-z0-9_]){20}(?!@))|(([A-Za-z0-9_]){1,19})(?![A-Za-z0-9_]*@))")
print("My new suggested re: ")
test_re(my_pattern)



