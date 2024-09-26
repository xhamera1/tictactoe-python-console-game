# Console Tic tac toe game in python for two people

import random

class MyException(Exception):
    pass

def check_win(game):
    # returned True means game is over and player won
    # returned False means nobody won yet
    # top-horizontal
    if game[0][0] == game[0][1] and  game[0][0] in ['X', 'O']:
        if game[0][1] == game[0][2]:
            return True
    # mid-horizontal
    if game[1][0] == game[1][1] and  game[1][0] in ['X', 'O']:
        if game[1][1] == game[1][2]:
            return True
    # bot-horizontal
    if game[2][0] == game[2][1] and  game[2][0] in ['X', 'O']:
        if game[2][1] == game[2][2]:
            return True
    # left-vertical
    if game[0][0] == game[1][0] and  game[0][0] in ['X', 'O']:
        if game[1][0] == game[2][0]:
            return True
    # mid-vertical
    if game[0][1] == game[1][1] and  game[0][1] in ['X', 'O']:
        if game[1][1] == game[2][1]:
            return True
    # right-vertical
    if game[0][2] == game[1][2] and  game[0][2] in ['X', 'O']:
        if game[1][2] == game[2][2]:
            return True
    # diagonal 1
    if game[0][0] == game[1][1] and  game[1][1] in ['X', 'O']:
        if game[1][1] == game[2][2]:
            return True
    # diagonal 2
    if game[0][2] == game[1][1] and  game[2][0] in ['X', 'O']:
        if game[1][1] == game[2][0]:
            return True
    return False

def convert_slot(slot):
    # convert int slot number to tuple of 2D cords
    match slot:
        case "1":
            return (0,0)
        case "2":
            return (0,1)
        case "3":
            return (0,2)
        case "4":
            return (1,0)
        case "5":
            return (1,1)
        case "6":
            return (1,2)
        case "7":
            return (2,0)
        case "8":
            return (2,1)
        case "9":
            return (2,2)
        case _:
            return (-1,-1)
        

def print_game(game):
    # prints currnet game table
    print(f"            |            |            ")
    print(f"     {game[0][0]}      |     {game[0][1]}      |      {game[0][2]}     ")
    print(f"            |            |            ")
    print(f"------------|------------|-----------")
    print(f"            |            |            ")
    print(f"     {game[1][0]}      |     {game[1][1]}      |      {game[1][2]}     ")
    print(f"            |            |            ")
    print(f"------------|------------|-----------")
    print(f"            |            |            ")
    print(f"     {game[2][0]}      |     {game[2][1]}      |      {game[2][2]}     ")
    print(f"            |            |            ")


def mark(player, slot, game):
    # marks chosen spot
    cords = convert_slot(slot)
    if cords == (-1, -1):
        raise ValueError("Invalid slot")
    if game[cords[0]][cords[1]] in ['X', 'O']:
        raise MyException("Chosen slot is already taken!")
    game[cords[0]][cords[1]] = player

def change_player(player):
    # changes player
    if player == "X":
        return "O"
    else:
        return "X"

def main():
    print("Let's start the game!")
    print("Choose who of you will be player X and player O")
    
    while True:
        try:
            ready = input("Are you ready? (yes/no): ")
            if ready.lower() == "yes":
                # Initialize the game board
                game = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]

                # Randomly decide who starts
                player = "X" if random.randint(0, 1) == 0 else "O"
                print(f"Player {player} starts!")
                print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
                print_game(game)

                # Game loop
                for _ in range(9):
                    while True:
                        try:
                            choice = input(f"Player {player}, choose a spot (1-9): ")
                            mark(player, choice, game)
                            print_game(game)
                            if check_win(game):
                                print(f"Player {player} won!!")
                                return
                            break
                        except MyException as e:
                            print(e)
                        except ValueError:
                            print("Invalid input. Please choose a number between 1 and 9.")

                    # Switch players after each valid turn
                    player = change_player(player)

                print("It's a draw!")
                return
            else:
                raise ValueError("Invalid input")
        except ValueError:
            print("Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()
