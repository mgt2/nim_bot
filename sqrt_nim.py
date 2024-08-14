from generate_win_table import generate_win_table
import numpy as np

def find_win_table_sqrt(outcomes_found, player1_wins, n) :
    if n >= 0 and outcomes_found[n] :
        return
    elif n <= 0 :
        player1_wins[n] = False
        outcomes_found[n] = True
        return
    elif n == 1 :
        player1_wins[n] = True
        outcomes_found[n] = True
        return
    else :
        moves = [i for i in range(1, int(n**0.5) + 1)]
        for move in moves :
            if n - move >= 0 :
                if not outcomes_found[n - move]:
                    find_win_table_sqrt(n - move, outcomes_found, player1_wins)
                if not player1_wins[n - move] :
                    player1_wins[n] = True
                    outcomes_found[n] = True
                    return
        player1_wins[n] = False
        return

def generate_sqrt_win_table(n) :
    outcomes_found = np.full(n + 1, False)
    player1_wins = np.full(n + 1, False)
    
    find_win_table_sqrt(n, outcomes_found, player1_wins)

    win_table = np.where(player1_wins, 1, 2)
    return win_table
