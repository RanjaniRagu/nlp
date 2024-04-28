import nltk
from nltk.util import ngrams
sentences = ["The weather is good we can play cricket"]
n = 3
for sentence in sentences:
 words = sentence.split()
 word_ngrams = ngrams(words, n)
 print(f"Word {n}-grams for sentence: '{sentence}'")
 for gram in word_ngrams:
 print(gram)
