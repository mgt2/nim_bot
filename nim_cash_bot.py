from bot_play import make_move, play_bot_game
from generate_win_table import generate_win_table
import random
import numpy as np
from nim_cash import generate_win_table_cash

def make_move_cash(n, moves, win_table, prob_correct_move, budget, opp_budget, player1_turn) :
    if random.random() < prob_correct_move :
        if (win_table[n] == 1) == (player1_turn) :
            for poss_move in moves :
                if n - poss_move >= 0 and budget >= poss_move:
                    new_win_table = generate_win_table_cash(moves, n - poss_move, [budget - poss_move, opp_budget])
                    if (new_win_table[n - poss_move] == 1) == (player1_turn) :
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
        if budgets[0] <= 0:
            return False
        elif budgets[1] <= 0:
            return True
        
        if player1_turn :
            move = make_move(n, moves, win_table, bot1_acc, budgets[0], budgets[1], player1_turn)
            budgets[0] -= move
        else :
            move = make_move(n, moves, win_table, bot2_acc, budgets[1], budgets[0], player1_turn)
            budgets[1] -= move
        n -= move
        if n == 0:
            return player1_turn
        
        player1_turn = not player1_turn
    return player1_turn