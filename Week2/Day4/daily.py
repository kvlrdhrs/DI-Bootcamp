class Text:
    def __init__(self, text):
        self.text = text
        self.words = self.text.split()
    
    def word_frequency(self, word):
        word_count = self.words.count(word)
        if word_count == 0:
            return f"The word '{word}' does not appear in the text."
        return word_count
    
    def most_common_word(self):
        word_counts = {}
        for word in self.words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        most_common = max(word_counts, key=word_counts.get)
        return most_common
    
    def unique_words(self):
        return list(set(self.words))
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

# Example usage with a text file
text_instance = Text.from_file('the_stranger.txt')
print("Frequency of 'the':", text_instance.word_frequency('the'))
print("Most common word:", text_instance.most_common_word())
print("Unique words:", text_instance.unique_words())