def init_grid(game):
    game['ch'] = [[' ' for _ in range(3)] for _ in range(3)]
    game['p1'] = 0
    game['p2'] = 0

def print_grid(game):
    print("\n")
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(f" {game['ch'][i][j]} |", end="")
            else:
                print(f" {game['ch'][i][j]} ")
        if i < 2:
            print("-----------")

def pos_maker(position):
    position -= 1
    row = position // 3
    column = position % 3
    return row, column

def check_win(game):
    symbols = ['X', 'O']
    for symbol in symbols:
        for i in range(3):
            if (game['ch'][i][0] == symbol and game['ch'][i][1] == symbol and game['ch'][i][2] == symbol) or \
               (game['ch'][0][i] == symbol and game['ch'][1][i] == symbol and game['ch'][2][i] == symbol):
                if symbol == 'X':
                    game['p1'] = 1
                    game['p2'] = 0
                else:
                    game['p1'] = 0
                    game['p2'] = 1
                return True
        if (game['ch'][0][0] == symbol and game['ch'][1][1] == symbol and game['ch'][2][2] == symbol) or \
           (game['ch'][0][2] == symbol and game['ch'][1][1] == symbol and game['ch'][2][0] == symbol):
            if symbol == 'X':
                game['p1'] = 1
                game['p2'] = 0
            else:
                game['p1'] = 0
                game['p2'] = 1
            return True
    return False

def winner(game, p1, p2, a, b):
    if game['p1'] == 1 and game['p2'] == 0:
        print(f"\n\nPlayer {p1} won the match🏆\n")
        a[0] += 1
    elif game['p1'] == 0 and game['p2'] == 1:
        print(f"\n\nPlayer {p2} won the match🏆\n")
        b[0] += 1
    else:
        print("\n\nMatch Draw🤣")
        a[0] += 1
        b[0] += 1

def set_winner(a, b, set_num, p1, p2):
    if a[0] > b[0]:
        print(f"\n\nPlayer {p1} Wins the {set_num} Set Game")
    elif b[0] > a[0]:
        print(f"\n\nPlayer {p2} Wins the {set_num} Set Game")
    else:
        print("Draw in Match")

def start_game():
    game = {}
    a = [0]
    b = [0]
    print("\n\n\t\tTic Tac Toe Game!\t\t\n\n")
    while True:
        try:
            set_num = int(input("How many sets you wanna play: "))
            if set_num <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                break  # Exit the loop if a valid number is entered
        except ValueError:
            print("Please enter a valid number.")
    p1 = input("Enter Player1 Name: ")
    p2 = input("Enter Player2 Name: ")
    for _ in range(set_num):
        init_grid(game)
        print("\n\nGAME STARTED :")
        print("\n\tTHE POSITIONS OF GRID IS :\n")
        print("\t     1 | 2 | 3 ")
        print("\t    -----------")
        print("\t     4 | 5 | 6 ")
        print("\t    -----------")
        print("\t     7 | 8 | 9 ")
        print("\nYou can't allocate for already used positions.\n")
        for i in range(9):
            if i % 2 == 0:
                print("\nP1(X) enter Position:")
            else:
                print("\nP2(O) enter Position:")
            while True:  # Loop until a valid position is entered
                try:
                    position = int(input())
                    if position < 1 or position > 9:
                        print("Please enter a number between 1 and 9.")
                    else:
                        row, column = pos_maker(position)
                        if game['ch'][row][column] == ' ':
                            break  # Exit loop if position is valid
                        else:
                            print("Position already taken. Please choose another position.")
                except ValueError:
                    print("Please enter a valid number.")
            if i % 2 == 0:
                game['ch'][row][column] = 'X'
            else:
                game['ch'][row][column] = 'O'
            print_grid(game)
            if check_win(game):
                break
        winner(game, p1, p2, a, b)
    set_winner(a, b, set_num, p1, p2)

def main():
    decision = input("START GAME (Y/N): ")
    if decision.upper() == 'Y':
        start_game()
    elif decision.upper() == 'N':
        print("I understand that You don't know how to play the game :)")
    else:
        print("Enter correct Input")


main()
