# Mini-Project - Tic Tac Toe
import numpy as np


board = np.full([3,3], "   ", dtype=str)



def display_board():
    header_game = 'Welcome to TIC TAC TOE! \n'
    row_name = '\nTIC TAC TOE \n'
    str1 = '*'*17
    str2 = '*---|---|---*'
    print(f"{header_game}{row_name}{str1}\n*  {board[0][0]}|{board[0][1]}|{board[0][2]}  *")

display_board()

def player_input(player):
    pass


def check_win():
    pass


def play():
    pass


