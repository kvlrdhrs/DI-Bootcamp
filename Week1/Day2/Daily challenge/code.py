#Challenge1

def generate_multiples(number, length):
    multiples_list = [number * i for i in range(1, length + 1)]
    return multiples_list

# Get user input
user_number = int(input("Enter a number: "))
user_length = int(input("Enter the desired length: "))

# Generate and print the list of multiples
result_list = generate_multiples(user_number, user_length)
print(result_list)





#Challenge2

def remove_consecutive_duplicates(input_string):
    result_string = ""
    for char in input_string:
        if not result_string or char != result_string[-1]:
            result_string += char
    return result_string

# Get user input
user_word = input("Enter a word: ")

# Remove consecutive duplicates and display the final string
final_string = remove_consecutive_duplicates(user_word)
print("Final string:", final_string)