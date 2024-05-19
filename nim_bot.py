import numpy as np
import random
from generate_win_table import generate_win_table

def ask_n () :
    n = int(input("Enter the number of sticks: "))
    return n

def ask_moves() :
    moves = input("Enter the moves you would like to use (separate by commas): ")
    moves = moves.split(',')
    moves = list(map(int, moves))
    return moves

def ask_user_turn() :
    user_input = input("Would you like to go first? (y/n/random) ")
    if user_input.lower() == "y" :
        user_turn = True
    elif user_input.lower() == "n" :
        user_turn = False
    else :
        rand_start = random.random()
        if rand_start < 0.5 :
            user_turn = True
        else :
            user_turn = False
    return user_turn

def calculate_strength(n, moves) :
    strength = int(input("What strength would you like the computer to play at? (integer 0-10) "))
    # If you want a more complex strength calculation, you can use the following code:
    expected_iters = n / np.mean(np.array(moves))
    return (strength/10)**(2/expected_iters)
    # Otherwise, just return strength/10
    # return strength/10


def play_nim() :
    print()
    print("-----------------------------------------------------------------------------------------------")
    print("Welcome to Nim!\n")
    print("Here are the rules: ")
    print("1. There are a certain number of sticks. (You can choose this number)")
    print("2. Each turn, you can take sticks. (You can choose how many sticks you are allowed to take)")
    print("3. Players take turns taking sticks. The player who takes the last stick wins.")
    print("4. Have fun!\n\n")

    n = ask_n()
    moves = ask_moves()
    user_turn = ask_user_turn()

    prob_correct_move = calculate_strength(n, moves)
    win_table = generate_win_table(moves, n)

    print("\nTime to play!")

    while True :
        print("\nThere are " + str(n) + " sticks left.")
        if user_turn :
            user_input = int(input("How many sticks would you like to take? "))
            if user_input in moves :
                n -= user_input
                if n == 0 :
                    again = input("You win! Do you want to play again? (y/n) ")
                    if again.lower() == "y" :
                        play_nim()
                    break
                elif n < 0 :
                    print("Invalid move. Please try again.")
                else :
                    user_turn = False
            else :
                print("Invalid move. Please try again.")
        else :
            if random.random() < prob_correct_move :
                if win_table[n] == 1 :
                    for poss_move in moves :
                        if n - poss_move >= 0 and win_table[n - poss_move] == 2 :
                            move = poss_move
                else :
                    valid_moves = []
                    for poss_move in moves :
                        if n - poss_move >= 0 :
                            valid_moves.append(poss_move)
                    move = random.choice(valid_moves)
            else :
                valid_moves = []
                for poss_move in moves :
                    if n - poss_move >= 0 :
                        valid_moves.append(poss_move)
                move = random.choice(valid_moves)
            print("The computer takes " + str(move) + " sticks.")
            n -= move
            if n == 0 :
                again = input("The computer wins! Do you want to play again? (y/n) ")
                if again.lower() == "y" :
                    play_nim()
                break
            user_turn = True


if __name__ == "__main__" :
    play_nim()