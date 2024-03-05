# Exercise 1 : What Are You Learning ?
def display_message():
    print("i'm learning python and how to survive in Israel without a job")


display_message()


# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Python")


# Exercise 3 : Some Geography
def describe_city(city, country='none'):
    print(f"{city} is in {country}")


describe_city('bat yam', 'israel')
describe_city('bat yam')  # checking default value

# Exercise 4 : Random
from random import randint, random


def compare_numbers(user_number):
    random_number = randint(1, 100)
    if user_number == random_number:
        print('success message')

    if user_number != random_number:
        print('fail message')
        print(f'{user_number} and {random_number}')


compare_numbers(23)


# Exercise 5 : Let’s Create Some Personalized Shirts !
def make_shirt(size='Large', text='I love Python'):
    print(f'The size of the shirt is {size} and the text is {text}')


make_shirt()  # Make a large shirt with the default message
make_shirt(size='Medium')  # Make medium shirt with the default message
make_shirt(size='Small', text='Python-Python')  # Make a shirt of any size with a different message.
make_shirt(size='1', text='0')

# Exercise 6 : Magicians …

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians():
    print('\n'.join(magician_names))


def make_great():
    for name in magician_names:
        print(f"{name} the Great")


make_great()
show_magicians()

# Exercise 7 : Temperature Advice
