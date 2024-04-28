import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
nltk.download('stopwords')
data="The best and most beautiful things in the world 
cannot be seen or even touched-they must be felt by heart" stopwords=set(stopwords.words('english')) 
words=word_tokenize(data.lower())
wordsFiltered=[] 
stopwords_list=[] 
for i in words:
if i not in stopwords: 
wordsFiltered.append(i)
else:
stopwords_list.append(i) 
print("Orginal words given:",data)
print("Stop words in given sentence:" ,stopwords_list) 
print("\nTotal Stop words: \n",stopwords) 
print("\nFiltered words: ",wordsFiltered)
