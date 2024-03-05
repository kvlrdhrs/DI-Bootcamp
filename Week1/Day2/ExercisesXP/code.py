#Exercise 1 : Set

my_fav_numbers = {23} # create a set
my_fav_numbers.add(666) # add smthng in a set
my_fav_numbers #we cant remove the last nunber in the set

friend_fav_numbers = [100,200,300,100,200,300,100,200,300,100,200,300,100,200,300,100,200,300,100,200,300] # create a list with duplicates
friend_fav_numbers = set(friend_fav_numbers)
friend_fav_numbers

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
our_fav_numbers





#Exercise 3: List

#remove items
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

list_to_remove = ('Banana', 'Blueberries')
for item in list_to_remove:
    basket.remove(item)
print(basket)
#add items
basket.append('Kiwi')
print(basket)

basket.insert(0, 'Apples')
print(basket)

#count apples
print(basket.count('Apples'))

#clear basket
basket.clear()

#print
print(basket)












#Exercise 4: Floats

#float is a type of obj. The main difference between an int and a float in the type of numbers they can represent.

num = 0.5
list1 = [x + num for x in range(1000) if x > 0 and x <=4]
list2 = [x for x in range(1000) if x > 1 and x <=5]
list3 = list1 + list2
list3.sort()
print(list3)


#another way to generate a sequence of floats







#Exercise 5: For Loop

for num in range(21):
    print(num)



for num in range(21):
        if num % 2 == 0:
            print(num)






#Exercise 6 : While Loop
my_name = 'Kanan'

while True:
    input_name = input("write your name")

    if input_name == my_name:
        print('good')
        break
    else:
        print("nope, try again")





#Exercise 7: Favorite Fruits

fav_fruit = input("enter your favorite fruit(s). separated by a single space")

fav_fruit_list = list(fav_fruit.split())

any_fruit = input("enter a name of any fruit")
if any_fruit in fav_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")






#Exercise 8: Who Ordered A Pizza ?

total_price = 10  # Base price for the pizza
toppings_list = []  # Use a list to store toppings

while True:
    toppings = input("Enter a pizza topping (type 'quit' to finish): ")

    if toppings.lower() == 'quit':
        break

    toppings_list.append(toppings)
    total_price += 2.5  # Add $2.5 for each topping
    print(f"You'll add {toppings} to your pizza.")

print("\nToppings on your pizza:")
for topping in toppings_list:
    print("- " + topping)

print(f"\nTotal price: ${total_price}")





#Exercise 9: Cinemax

def calculate_ticket_cost(age):
    if age < 3:
        return 0
    elif 3 < age < 12:
        return 10
    elif age > 12:
        return 15
    

#calculate the total cost of family tickets
num_people = int(input("enter the number of people in the family"))
total_cost = 0

for _ in range(num_people):
    person_age = int(input("enter the age of a person"))
    total_cost +=calculate_ticket_cost(person_age)

print(f"total cost for the family tickets {total_cost}")



teenagers = ["test1", "test2", "test3", "test4", "test4"]

for teen in teenagers[:]:  # Iterate over a copy of the list to avoid modifying it while iterating
    age = int(input(f"Enter the age of {teen}: "))
    
    if not (16 <= age <= 21):
        teenagers.remove(teen)
        print(f"Sorry, {teen} is not permitted to watch the movie.")

print("\nFinal list of teenagers permitted to watch the movie:")
print(teenagers)