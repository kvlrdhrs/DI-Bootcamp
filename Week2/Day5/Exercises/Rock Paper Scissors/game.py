import random


class Game:
    def __init__(self):
        self.choices = ['r', 'p', 's']

    def get_user_item(self):
        while True:
            user_item = input("Select (r)ock, (p)aper, or (s)cissors: ")
            if user_item in self.choices:
                return user_item

    def get_computer_item(self):
        computer_item = random.choice(self.choices)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == 'r' and computer_item == 's':
            return "win"
        elif user_item == 'p' and computer_item == 'r':
            return "win"
        elif user_item == 's' and computer_item == 'p':
            return "win"
        else:
            return "loss"

    def play(self):
        get_user_item = self.get_user_item()
        get_computer_item = self.get_computer_item()
        game_result = self.get_game_result(get_user_item,get_computer_item)
        print(f"Your chose: {get_user_item}. The computer chose: {get_computer_item}. Result: {game_result}")
        return game_result