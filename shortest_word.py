# Given a set of words, find the shortest word. If there are mutiples, find the first one ordered by the letters
def shortest_word(words):
	# first, initialize the result (randomly picked from set)
	# second, you need to loop through the set, and compare the word with the result
	# 	compare with lenght, if shorter, then replace the result
	#												 if longer, then don't do anythin, just continue the loop (this can skipped)
	#												 if equal, then compare the word with result using <, or >, then replace the result if less
	# after the loop, the result is the answer
	result = words.pop()
	for word in words:
		if len(word) < len(result):
			result = word
		elif len(word) == len(result):
			if word < result:
				result = word
	return result

# words = {"alssls", "slskdkdd", "skskdkdk", "work", "abcd", "aksksk", "skdkdk"}
words = {'aaaa', 'bbb', 'cc', 'ca'} 
print(shortest_word(words))