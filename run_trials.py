from nim_cash_bot import play_cash_game, play_func_game
from sqrt_nim import generate_win_table
import numpy as np
def run_trials(n, moves, bot1_acc, bot2_acc, budgets, num_trials=100, nonfunc=True) :
    if nonfunc :
        trials = [play_cash_game(bot1_acc, bot2_acc, moves, n, budgets) for _ in range(num_trials)]
    else :
        trials = [play_func_game(bot1_acc, bot2_acc, moves_func, n) for _ in range(num_trials)]
    return trials

if __name__ == "__main__" :
    bot1_acc = float(input("Enter the accuracy of bot 1 (scale of 0 to 1): "))
    bot2_acc = float(input("Enter the accuracy of bot 2 (scale of 0 to 1): "))
    nonfunc = False
    budgets = [0,0]
    moves = input("Enter the moves, separated by commas. If you want moves to obey a function, select type log, sqrt, or exponential: ")
    if moves == "log":
        moves_func = lambda x: max(int(np.log(x)), 1)
    elif moves == "sqrt":
        moves_func = lambda x: int(np.sqrt(x))
    elif moves == "exponential":
        input_a = float(input("Enter the value of the exponent you want. This value must be less than 1: "))
        moves_func = lambda x: int(x ** input_a)
    else:
        budgets = input("Enter the budgets, separated by commas. If you do not want to play a cash game, provide budgets equal to n: ").split(",")

        # Convert the moves and budgets to integers
        moves = [int(move) for move in moves]
        budgets = [int(budget) for budget in budgets]
        nonfunc = True
    n = int(input("Enter the starting number of sticks: "))
    num_trials = int(input("Enter the number of trials: "))

    trials = run_trials(n, moves, bot1_acc, bot2_acc, budgets, num_trials, nonfunc)
    # print(trials)
    print("Player 1 wins " + str(np.sum(trials)) + " of " + str(num_trials) + " games")
    
    # print("Done")