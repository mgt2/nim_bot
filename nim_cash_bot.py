from bot_play import make_move, play_bot_game
from generate_win_table import generate_win_table
import random
import numpy as np

def make_move_cash(n, moves, win_table, prob_correct_move, budget, opp_budget) :
    if random.random() < prob_correct_move :
        if budget * 2 < n or opp_budget * 2 < n:
            move = 1

        elif budget >= n :
            if win_table[n] == 1 :
                for poss_move in moves :
                    if n - poss_move >= 0 and win_table[n - poss_move] == 2 and budget >= poss_move:
                        move = poss_move
                        return move
            else :
                move = 1
        else :
            if budget < opp_budget :
                if win_table[n] == 1 :
                    for poss_move in moves :
                        if n - poss_move >= 0 and win_table[n - poss_move] == 2 and budget >= poss_move:
                            move = poss_move
                        return move
                return 1
            
            else :
                if win_table[n] == 1 :
                    for poss_move in moves :
                        if n - poss_move >= 0 and win_table[n - poss_move] == 2 and budget >= poss_move and budget - opp_budget >= poss_move:
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
    win_table = generate_win_table(moves, n)
    player1_turn = True

    if n <= 0 or budgets[0] <= 0:
        return False
    
    while n > 0 :
        if budgets[0] <= 0:
            return False
        elif budgets[1] <= 0:
            return True
        
        if player1_turn :
            move = make_move(n, moves, win_table, bot1_acc, budgets[0], budgets[1])
            budgets[0] -= move
        else :
            move = make_move(n, moves, win_table, bot2_acc, budgets[1], budgets[0])
            budgets[1] -= move
        n -= move
        if n == 0:
            return player1_turn
        
        player1_turn = not player1_turn
    return player1_turn