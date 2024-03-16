# Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal = Bengal('BengalCat', 3)
siamese = Siamese('SiameseCat', 10)
chartreux = Chartreux('ChartreuxCat', 1)

all_cats = [bengal, siamese, chartreux]
sara_pets = Pets(all_cats)

sara_pets.walk()


# Exercise 2 : Dogs
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return self.name + " is barking!"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return self.name + ' won the fight'
        if other_score > self_score:
            return other_dog.name + ' won the fight'
        else:
            return 'Its a draw'


dog1 = Dog('Dog1', 23, 10)
dog2 = Dog('Dog2', 10, 5)
dog3 = Dog('Dog3', 10, 40)

print(dog1.fight(dog3))


# Exercise 3 : Dogs Domesticated
# ex.3 in the another file 'XP(ex.3)

# Exercise 4 : Family

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **members):
        self.members.append(members)
        print(f"Congratulations! {members['name']} is born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
            else:
                return False

    def family_presentation(self):
        print(self.last_name)
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']},"
                  f"{' Adult' if not member['is_child'] else ' Child'}")


family = Family('Johns', [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

family.born(name='Python', age=0, gender='Male', is_child=True)
family.family_presentation()


# Exercise 5 : TheIncredibles Family

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        # Call the parent class's constructor
        super().__init__(last_name, members)

    def use_power(self, member_name):
        # Find the member
        for member in self.members:
            if member['name'] == member_name:
                # Check if the member is over 18
                if member['age'] > 18:
                    print(f"{member_name} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member_name} is not over 18 years old.")
                break

    def incredible_presentation(self):
        # Print the introduction
        print("Here is our powerful family:")
        # Print the family's last name and all the members' details
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']},"
                  f"{' Adult' if not member['is_child'] else ' Child'}, Power: {member['power']}, Incredible Name: {member['incredible_name']}")


# Create an instance of the Incredibles class
incredibles = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
     'incredible_name': 'SuperWoman'}
])

incredibles.incredible_presentation()

# Use the born method to add Baby Jack
incredibles.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='Baby Jack')

# Call the incredible_presentation method again
incredibles.incredible_presentation()
