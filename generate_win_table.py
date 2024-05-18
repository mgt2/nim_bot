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

def find_win_condition(win_table) :
    condition = np.where(win_table == 1, True, False)
    condition = np.where(condition)[0]
    return condition

if __name__ == "__main__" :
    moves = [1, 3, 4]
    n = 10
    win_table = generate_win_table(moves, n)
    print(win_table)
    print(find_win_condition(win_table))
    print("Done")