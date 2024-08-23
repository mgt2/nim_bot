from generate_win_table import generate_win_table
import numpy as np

def find_win_table_sqrt(n, outcomes_found, player1_wins, moves_func) :
    # print(n)
    moves = [i for i in range(1, int(moves_func(n)) + 1)]
    if n >= 0 and outcomes_found[n] :
        return
    elif n <= 0 :
        player1_wins[n] = False
        outcomes_found[n] = True
        return
    elif n == 1 and moves != []:
        player1_wins[n] = True
        outcomes_found[n] = True
        return
    else :
        for move in moves :
            if n - move >= 0 :
                if not outcomes_found[n - move]:
                    find_win_table_sqrt(n - move, outcomes_found, player1_wins, moves_func)
                if not player1_wins[n - move] :
                    player1_wins[n] = True
                    outcomes_found[n] = True
                    return
        player1_wins[n] = False
        return

def sqrt_moves(n) :
    return n ** 0.5

def log_moves(n) :
    return np.log(n)

def exponential_moves(n, a) :
    if a > 1:
        return RuntimeError("a must be less than or equal to 1")
    return n ** a

def generate_sqrt_win_table(n, moves_func) :
    outcomes_found = np.full(n + 1, False)
    player1_wins = np.full(n + 1, False)
    
    find_win_table_sqrt(n, outcomes_found, player1_wins, moves_func)

    win_table = np.where(player1_wins, 1, 2)
    return win_table
