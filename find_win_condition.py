import numpy as np
def find_win_condition(win_table) :
    condition = np.where(win_table == 1, True, False)
    condition = np.where(condition)[0]
    return condition