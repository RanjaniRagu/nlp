import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.wsd import lesk
from pywsd.lesk import simple_lesk
sentences = [
 "She watched the bass swim in the clear water.",
 "The bass was playing in the band at the concert.",
 "He caught a big bass while fishing in the lake."
]
for sentence in sentences:
 print("Context:", sentence)
 target_word = "bass"
 meaning = simple_lesk(sentence, target_word)
 if meaning:
 sense = meaning.definition()
 print("Sense:", sense)
 else:
 print("Sense not found")
