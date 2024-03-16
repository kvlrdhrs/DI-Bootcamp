import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class AnagramChecker():
    def __init__(self):
        with open(dir_path + '\\sowpods.txt', 'r') as file_obj:
            self.dict = [word.strip() for word in file_obj.readlines()]

    def is_valid_word(self, word):
        if word.upper() not in self.dict:
            return False
        else:
            return True

    def is_anagram(self, word1, word2):
        if word1.lower() != word2.lower() and sorted(word1.lower()) == sorted(word2.lower()):
            return True
        else:
            return False

    def get_anagrams(self, word):
        anagrams_list = []
        for dict_word in self.dict:
            if self.is_anagram(dict_word, word):
                anagrams_list.append(dict_word)
        return anagrams_list
