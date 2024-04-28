import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
def tokenize_text(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return words, sentences
sample_text = "Tokenization is a key step in natural language processing. It breaks text into smaller units."
word_tokens, sentence_tokens = tokenize_text(sample_text)
print("Word Tokens:")
for token in word_tokens:
    print(token)
print("\nSentence Tokens:")
for token in sentence_tokens:
    print(token)

