from random import randint


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
make_shirt('Medium')  # Make medium shirt with the default message
make_shirt('Small', '')  # Make a shirt of any size with a different message.
make_shirt(size='1', text='0')  # bonus

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
def get_random_temp(season):
    if season.lower() == 'summer':
        return randint(20, 45)
    elif season.lower() == 'winter':
        return randint(-10, 20)
    else:
        return randint(5, 30)


def main():
    user_season = input('What season would you like to:')
    temperature = get_random_temp(user_season)
    print(f'The temperature right now is {temperature} degrees Celsius')
    if temperature < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0 < temperature < 16:
        print('Quite chilly! Don’t forget your coat')

    elif 16 <= temperature <= 23:
        print('Test2')

    elif 24 <= temperature <= 32:
        print('Test3')

    else:
        print('Test4')


main()


# Exercise 8 : Star Wars Quiz
def quiz_question():
    for question, answer in data.items():
        print(question)
        user_answer = input("")
        if user_answer != answer:
            print("Sorry")
quiz_question()



data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]