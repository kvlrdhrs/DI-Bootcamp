from game import Game

def get_user_menu_choice():
    print("    Menu:")
    user_menu = input('(g) Play a new game \n(x) Show scores \n(e) Exit game\n: ')
    if user_menu in ['g', 'x', 'e']:
        return user_menu
    else:
        raise TypeError("Invalid input")

def print_result(results):
    print("Game Results:")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")
    print("\nThank you for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == 'g':
            game = Game()
            game_result = game.play()
            results[game_result] += 1
        elif user_choice == 'x':
            print_result(results)
        elif user_choice == 'e':
            print_result(results)
            break

main()
