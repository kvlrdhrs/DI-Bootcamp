import numpy as np

board = np.full([3, 3], "-", dtype=str)
player1 = 'X'
player2 = 'O'
current_player = player1  # Start with player1
winner = None
game_active = True


def display_board():
    header_game = 'Welcome to TIC TAC TOE! \n'
    row_name = '\nTIC TAC TOE \n'
    str1 = '*' * 17
    str2 = '*---|---|---*'
    print(f"{header_game}{row_name}{str1}\n{board[0]}\n{board[1]}\n{board[2]}\n{str1}")


def player_input():
    global current_player

    input1 = int(input('Enter row:'))
    input2 = int(input('Enter column'))

    if input1 in range(1, 4) and input2 in range(1, 4):
        if board[input1 - 1][input2 - 1] == '-':
            board[input1 - 1][input2 - 1] = current_player
            # Switch to the other player for the next turn
            current_player = player2 if current_player == player1 else player1
        else:
            print('Cell already occupied. Try again.')
    else:
        print('Invalid input. Please enter values between 1 and 3 for both row and column.')

    print(board)


def check_win():
    global winner

    # Check rows
    for row in board:
        if all(cell == player1 for cell in row):
            winner = player1
            return True
        elif all(cell == player2 for cell in row):
            winner = player2
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player1 for row in range(3)):
            winner = player1
            return True
        elif all(board[row][col] == player2 for row in range(3)):
            winner = player2
            return True

    # Check diagonals
    if all(board[i][i] == player1 for i in range(3)) or all(board[i][2 - i] == player1 for i in range(3)):
        winner = player1
        return True
    elif all(board[i][i] == player2 for i in range(3)) or all(board[i][2 - i] == player2 for i in range(3)):
        winner = player2
        return True

    return False


def is_board_full():
    return all(cell != '-' for row in board for cell in row)


display_board()

while game_active:
    if check_win():
        print(f"Player {winner} wins!")
        game_active = False
    elif is_board_full():
        print("It's a tie!")
        game_active = False
    else:
        display_board()
        player_input()
