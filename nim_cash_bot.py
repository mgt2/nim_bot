from bot_play import make_move, play_bot_game
from generate_win_table import generate_win_table
import random
import numpy as np
from nim_cash import generate_win_table_cash
from sqrt_nim import generate_sqrt_win_table


def play_func_game(bot1_acc, bot2_acc, moves_func, n):
    player1_turn = True
    win_table = generate_sqrt_win_table(n, moves_func)
    if n <= 0:
        return False

    while n > 0:
        moves = [i for i in range(1, int(moves_func(n)) + 1)
             if n - i >= 0]
        if player1_turn:
            move = make_move(n, moves, win_table, bot1_acc)
        else:
            move = make_move(n, moves, win_table, bot2_acc)
        n -= move
        if n == 0:
            return player1_turn
        player1_turn = not player1_turn
    return player1_turn


def make_move_cash(n, moves, win_table, prob_correct_move, budget, opp_budget, player1_turn) :
    if random.random() < prob_correct_move :
        for poss_move in moves :
            # print(poss_move)
            if n - poss_move >= 0 and budget >= poss_move:
                new_win_table = generate_win_table_cash(moves, n - poss_move, [opp_budget, budget - poss_move])
                # print(new_win_table)
                if (new_win_table[n - poss_move] == 2) :
                    move = poss_move
                    return move
        return 1

    else :
        valid_moves = []
        for poss_move in moves :
            if n - poss_move >= 0 and budget >= poss_move:
                valid_moves.append(poss_move)
        move = random.choice(valid_moves)
        return move

def play_cash_game(bot1_acc, bot2_acc, moves, n, budgets):
    player1_turn = True

    if n <= 0 or budgets[0] <= 0:
        return False
    
    while n > 0 :
        win_table = generate_win_table_cash(moves, n, budgets)
        # print(budgets)
        if budgets[0] <= 0:
            return False
        elif budgets[1] <= 0:
            return True
        
        if player1_turn :
            move = make_move_cash(n, moves, win_table, bot1_acc, budgets[0], budgets[1], player1_turn)
            # print(move)
            budgets[0] -= move
        else :
            move = make_move_cash(n, moves, win_table, bot2_acc, budgets[1], budgets[0], player1_turn)
            budgets[1] -= move
            # print(move)
        n -= move
        if n == 0:
            return player1_turn
        
        player1_turn = not player1_turn
    return player1_turn


if __name__ == "__main__" :
    bot1_acc = float(input("Enter the accuracy of bot 1 (scale of 0 to 1): "))
    bot2_acc = float(input("Enter the accuracy of bot 2 (scale of 0 to 1): "))
    moves = input("Enter the moves, separated by commas: ").split(",")
    budgets = input("Enter the budgets, separated by commas: ").split(",")

    # Convert the moves and budgets to integers
    moves = [int(move) for move in moves]
    budgets = [int(budget) for budget in budgets]
    n = int(input("Enter the starting number of sticks: "))
    print(play_cash_game(bot1_acc, bot2_acc, moves, n, budgets))
    # print("Done")