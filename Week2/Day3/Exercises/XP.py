# Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}' if self.amount == 1 else f'{self.amount} {self.currency}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}' if self.amount == 1 else f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.amount + other
        elif isinstance(other, Currency) and self.currency == other.currency:
            return self.amount + other.amount
        elif isinstance(other, Currency) and self.currency != other.currency:
            print(f'Cannot add {other.currency} to {self.currency}')
        else:
            raise TypeError(f'ERROR')

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return self

        elif isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
            return self
        else:
            raise TypeError(f'ERROR')


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 +=5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)

# Exercise 2: Import

# Exercise 3: String Module
import string
import random

random_string = ''.join(random.choices(string.ascii_letters, k=5))
print(random_string)

# Exercise 4 : Current Date

from datetime import datetime

def display_current_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

# Call the function to display the current date
display_current_date()

# Exercise 5 : Amount Of Time Left Until January 1st

from datetime import timedelta

def time_until_january_1st():
    current_date = datetime.now()
    january_1st = datetime(current_date.year + 1, 1, 1)

    time_left = january_1st - current_date

    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    print(f"The 1st of January is in {days_left} days and {hours_left}:{minutes_left:02}:{seconds_left:02} hours.")

# Call the function to display the time until January 1st
time_until_january_1st()

# Exercise 6 : Birthday And Minutes
from datetime import datetime

def minutes_lived(birthdate):
    birth_datetime = datetime.strptime(birthdate, "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    minutes_lived = int((current_datetime - birth_datetime).total_seconds() / 60)

    print(f"You have lived for approximately {minutes_lived:.2f} minutes.")

birthdate_input = "1995-08-23 12:00:00"
minutes_lived(birthdate_input)

# Exercise 7 : Faker Module

from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Create an empty list called users
users = []

# Function to add new dictionaries to the users list
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code(),
    }
    users.append(user)

# Generate and add 5 fake users to the list
for _ in range(5):
    add_user()
print(users)
