from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
ps = PorterStemmer()
sentence = “The majestic mountains provide a breathtaking view”
words=word_tokenize(sentence)
for word in words:
	stemmed_word=ps.stem(word)
	print(word,”:”,stemmed_word)
