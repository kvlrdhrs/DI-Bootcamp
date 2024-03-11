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
chartreux = Chartreux('ChartreuxCat',1)

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
        return self.weight / self.age*10

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


# Exercise 4 : Family


# Exercise 5 : TheIncredibles Family
