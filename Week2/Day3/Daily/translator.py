# Daily Challenge: Translator
from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator()

translated_dict = {}

for word in french_words:
    translation = translator.translate(word, dest='en').text
    translated_dict[word] = translation

print(translated_dict)
