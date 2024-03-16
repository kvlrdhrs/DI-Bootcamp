import pandas as pd
import io
import requests
import json

class Text():
    def __init__(self, input_text):
        self.text = input_text

    def word_frequency(self, word):
        word_count = self.text.split().count(word)
        return f"The word '{word}' appears {word_count} times in the text."

    def common_word(self):
        words = self.text.split()
        common_word = max(set(words), key=words.count)
        return f"The most common word in the text is '{common_word}'."

    def unique_words(self):
        unique_words_list = list(set(self.text.split()))
        return f"The unique words in the text are: {', '.join(unique_words_list)}."

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
        return cls(file_content)

# Part I
input_text = "A good book would sometimes cost as much as a good house."
text_instance = Text(input_text)

print(text_instance.word_frequency("good"))
print(text_instance.common_word())
print(text_instance.unique_words())

# Part II
url = 'https://raw.githubusercontent.com/devtlv/theStranger_text_W5D4PY/34067ff2ada385c067fdfb365c6806b68751704f/the_stranger.txt'
response = requests.get(url)
text_data = response.text

text_instance_from_file = Text.from_file('the_stranger.txt')
print(text_instance_from_file.word_frequency("stranger"))


