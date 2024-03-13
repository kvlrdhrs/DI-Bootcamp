# Exercise 1 – Random Sentence Generator
import pandas as pd
import random as rd


def get_words_from_file():
    words_list = pd.read_csv("http://norvig.com/ngrams/sowpods.txt", header=None)
    words_list = words_list[0].tolist()
    return words_list


def get_random_sentence(words, length):
    random_words = rd.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence


def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program will generate a random sentence for you.")

    # Ask the user for input and validate it
    while True:
        try:
            sentence_length = int(input("Enter the length of the sentence (between 2 and 20): "))
            if 2 <= sentence_length <= 20:
                break
            else:
                print("Please enter a valid integer between 2 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Get the words list from the file
    words = get_words_from_file()

    # Generate and print the random sentence
    random_sentence = get_random_sentence(words, sentence_length)
    print("\nRandom Sentence:", random_sentence)


main()

# Working With JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# # Load JSON string into a Python dictionary
# data = json.loads(sampleJson)
#
# # Access the nested "salary" key
# print(data["company"]["employee"]["payable"]["salary"])
# # Add a new key "birth_date" at the same level as the "name" key
# data["company"]["employee"]["birth_date"] = "1995-08-23"  # You can replace this date with the actual birth date
#
# # Save the modified dictionary as JSON to a file
# with open("modified_data.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)
#
# print("JSON saved to 'modified_data.json'")
