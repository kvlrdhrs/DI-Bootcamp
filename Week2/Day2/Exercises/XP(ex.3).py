from XP import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained


    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            print(f"{self.name} does a barrel roll")
            print(f"{self.name} stands on his back legs")
            print(f"{self.name} shakes your hand")
            print(f"{self.name} plays dead")

pet_dog = PetDog('Kevin', 20, 10)
pet_dog.train()
pet_dog.play('Dog1', 'Dog2', 'Dog3', 'Kevin')
pet_dog.do_a_trick()