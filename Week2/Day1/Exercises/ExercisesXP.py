# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Arya", 2)
cat2 = Cat("Sad", 3)
cat3 = Cat("Kanan", 36)

my_list = [cat1, cat2, cat3]


def oldest_cat(my_list):
    oldest = max(my_list, key=lambda cat: cat.age)
    return oldest


oldest_cat_instance = oldest_cat(my_list)
print(f"The oldest cat is: {oldest_cat_instance.name} with age {oldest_cat_instance.age}")


# Exercise 2 : Dogs

class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')


davids_dog = Dog('Rex', 50)
print(f'The davids dog is {davids_dog.name}, hes height is {davids_dog.height}')
davids_dog.bark(), davids_dog.jump()

kanans_dog = Dog('Test1', 100)
Mashas_dog = Dog('Test2', 20)
Aryas_dog = Dog('Test3', 989)

dogs_list = [davids_dog, kanans_dog, Mashas_dog, Aryas_dog]


def biggest_dog(dogs_list):
    biggest = max(dogs_list, key=lambda dog: dog.height)
    return biggest


biggest_dog_instance = biggest_dog(dogs_list)
print(f'The biggest dog is {biggest_dog_instance.name}, hes height is {biggest_dog_instance.height}')


# Exercise 3 : Who’s The Song Producer?

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo

class Zoo():
    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name

    def add_animal(self,*new_animal):
        for animal in new_animal:
            if animal not in self.animals:
                self.animals.append(animal)


    def get_animal (self):
        print(self.animals)


    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)


    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)

        return grouped_animals



my_zoo = Zoo("Zoo_Test")
my_zoo.add_animal('Tiger', 'Ape', 'Baboon', 'Bear', 'Cat', 'Cougar', 'Eul', 'Emu')
my_zoo.sell_animal("Tiger")


my_zoo.get_animal()

sorted_and_grouped_animals = my_zoo.sort_animals()
print(sorted_and_grouped_animals)


    def get_groups(animals):
        pass


ramat_gan_safari = ''







