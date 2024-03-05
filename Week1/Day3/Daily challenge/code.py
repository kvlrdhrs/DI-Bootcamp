# Daily Challenge: Dictionaries

# challenge 1
word = input("Enter a word: ")

letter_indexes = {}

for index, letter in enumerate(word):
    # Ensure the letter is a string
    letter = str(letter)

    # If the letter is not already in the dictionary, add it with an empty list as the value
    letter_indexes.setdefault(letter, []).append(index)

# Print the resulting dictionary
print(letter_indexes)

# challenge 2
