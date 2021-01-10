# TicTacToe with functions

# Create board and game
import tictactoe_function as tf

pole = [0, '1', '2', '3', '4', '5', '6', '7', '8', '9']
pole_bot = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

count_number = 0
player_symbol = 'X'
bot_symbol = "O"
winner = "*"
turn = 'X'
choice = ''

tf.show_table(pole)

while count_number < 9:
    # X turn
    flag = True
    while flag:
        choice = str(input("Enter number of cell : "))
        for i in range(len(pole)):
            if choice == pole[i]:
                pole_bot.remove(pole[i])
                pole[i] = turn
                flag = False
                break

    winner = tf.check_winner(pole,winner)

    # Counter of step
    count_number = count_number + 1
    if count_number >= 9:
        break
    elif winner != '*':
        break

    tf.show_table(pole)

    turn = tf.change_turn(turn)

    pole,pole_bot = tf.bot_choice(pole,pole_bot,turn)

    # Counter of step
    count_number = count_number + 1
    if count_number >= 9:
        break
    elif winner != '*':
        break

    tf.show_table(pole)

    winner = tf.check_winner(pole,winner)

    turn = tf.change_turn(turn)
if winner == '*':
    print("Toe")
else:
    print(f'{winner} won the game !')