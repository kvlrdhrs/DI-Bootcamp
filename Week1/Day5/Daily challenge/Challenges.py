# Challenge 1 : Sorting
def sort_sentence(input_sentence):
    sorted_sentence = sorted([word.strip() for word in input_sentence.split(',')])
    return sorted_sentence


input_sentence = input('Enter a sentence: ')
print(sort_sentence(input_sentence))

# Challenge 2 : Longest Word
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest


sentence = input('Enter a sentence: ')
print(longest_word(sentence))





