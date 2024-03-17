import datetime
import calendar

# Get the birthdate from the user
birthdate = input("Enter your birthdate (format: DD/MM/YYYY): ")
birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y")

# Calculate the age
now = datetime.datetime.now()
age = now.year - birthdate.year
if now.month < birthdate.month or (now.month == birthdate.month and now.day < birthdate.day):
    age -= 1

# Determine the number of candles
candles = int(str(age)[-1])

# Check for leap year
leap_year = calendar.isleap(birthdate.year)

# Display the cake(s)
cake = f"""
       ___{'i'*candles}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
print(cake)
if leap_year:
    print("Bonus cake for being born in a leap year!")
    print(cake)
