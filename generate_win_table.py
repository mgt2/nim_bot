import numpy as np
def find_win_table(moves, outcomes_found, player1_wins, n, depth) :
    if n >= 0 and outcomes_found[n] :
        return
    elif n <= 0 :
        player1_wins[n] = False
        outcomes_found[n] = True
        return
    elif n == 1:
        player1_wins[n] = True
        outcomes_found[n] = True
        return
    else :
        #print("HERE", n, player1_wins[n], depth)
        for move in moves :
            if n - move >= 0 :
                if not outcomes_found[n - move]:
                    find_win_table(moves, outcomes_found, player1_wins, n - move, depth + 1)
                if not player1_wins[n - move] :
                    player1_wins[n] = True
                    outcomes_found[n] = True
                    return
    player1_wins[n] = False
    return

def generate_win_table(moves, n) :
    outcomes_found = np.full(n + 1, False)
    player1_wins = np.full(n + 1, False)

    find_win_table(moves, outcomes_found, player1_wins, n, 0)

    win_table = np.where(player1_wins, 1, 2)
    return win_table