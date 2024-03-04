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