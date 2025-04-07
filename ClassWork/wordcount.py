words = "hawanat was defining a dictionary and kept repeating dict the class had to encourage her to reduce the use of the word dict"
wordcount = {}
for word in words.split():
	if word in wordcount:
		wordcount[word] +=1
	else:
		wordcount[word] = 1

#for key, value in wordcount.items():
#	print(key, value)
word_count = {'word': words.count(word) for word in words.split()}
print(word_count)

