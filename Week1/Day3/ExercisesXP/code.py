# Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {key: value for key, value in zip(keys, values)}
print(dict)


# Exercise 2 : Cinemax
def calculate_ticket_cost(age):
    # create a function to calculate ticket cost by age
    if age < 3:
        return 0
    if 3 <= age <= 12:
        return 10
    else:
        return 15


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# calculate ticket cost for each family member
for keys, values in family.items():
    print(f"the ticket price for {keys} is {calculate_ticket_cost(values)}")

# calculate total tickets cost
values_list = list(family.values())
ticket_cost = 0
for value in values_list:
    ticket_cost += calculate_ticket_cost(value)
print(f"total ticket cost for family: {ticket_cost}")

# Exercise 3: Zara
brand = {'name': 'Zara', 'creation_date': '1975', 'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': '2', 'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green'],
    }}

# changing the number_stores
print(brand)

# describing zara's clients
for keys, values in brand.items():
    if keys == 'type_of_clothes':
        print(f"Zara's clients are {values}")

# add new key in dictionary
brand['country_creation'] = 'Spain'

# task 6, add new store with if
for keys, values in brand.items():
    if keys == 'international_competitors':
        brand['international_competitors'].append('Desigual')

# delete some info using pop
brand.pop('creation_date')
print(brand)

# print the last international competitor
print(brand['international_competitors'][-1])

# print the major clothes in the us
print(brand['major_color']['US'])

# print len of this dictionary
print(len(brand))

# print the keys of this dictionary
for keys in brand.keys():
    print(keys)

# create new dictionary
more_on_zara = {
    'creation_date': '1975',
    'number_stores': '10 000',
}

# add the info from one dictionary to another
brand.update(more_on_zara)
print(brand['number_stores'])
# the key in the 'number_stores' was updated also we added new (old) key 'creation_date'


# Exercise 4 : Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# 1st result
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)

# 2nd result
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)

# 3rd result
disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_users_C)

# 4th result
disney_users_A = {user: index for index, user in enumerate(users) if 'i' in user.lower()}
print(disney_users_A)

# 5th result
disney_users_A = {user: index for index, user in enumerate(users) if user.lower().startswith(('m', 'p'))}
print(disney_users_A)