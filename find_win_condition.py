import numpy as np
from generate_win_table import generate_win_table
def find_win_condition(win_table) :
    condition = np.where(win_table == 1, True, False)
    condition = np.where(condition)[0]

    ordered_list = np.array(range(len(win_table)))
    for i in range(2, len(win_table)) :
        mod_ordered = ordered_list % i

        accounted_for = condition.copy()
        total_merged = []
        for j in range(i) :
            if np.all(np.in1d(np.where(mod_ordered == j)[0], accounted_for)) :
                accounted_for = np.setdiff1d(accounted_for, np.where(mod_ordered==j)[0], assume_unique=False)
                total_merged.append(j)
            if len(accounted_for) == 0 :
                return total_merged, i
                
    return total_merged

def interpret_win_condition(win_table) :
    condition, mod_num = find_win_condition(win_table)
    print("Player 1 wins iff n=" + ', '.join(map(str, condition)) + " mod " + str(mod_num))
    return
    

def find_wins_all(moves, n) :
    win_table = generate_win_table(moves, n)
    string = "For moves: "
    for move in moves :
        string += str(move) + ", "
    string += ": "
    print(string)
    interpret_win_condition(win_table)
    print()
    print()
    return

if __name__ == "__main__" :
    moves = [1, 10, 11]
    n = 100
    win_table = generate_win_table(moves, n)
    # print(win_table)
    find_wins_all(moves, n)

        


