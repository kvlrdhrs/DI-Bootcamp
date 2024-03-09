
# creating the board
header_game = 'Welcome to TIC TAC TOE! \n'
# elements of the board
row_name = 'TIC TAC TOE'
eq1 = '---'
eq2 = '---'
eq3 = '---'
eq4 = '---'
eq5 = '---'
eq6 = '---'
eq7 = '   '
eq8 = '   '
eq9 = '   '

str1 = '*' * 17
str2 = '*     |   |     *'
str3 = f'*  {eq1}|{eq2}|{eq3}  *'
str4 = f'*  {eq4}|{eq5}|{eq6}  *'
str5 = f'*  {eq7}|{eq8}|{eq9}  *'
board = (row_name, str1, str2, str3, str2, str4, str5, str1)

show_board = [print(i) for i in board]

# players inputs


turn1 = int(input('Enter row: '))
0