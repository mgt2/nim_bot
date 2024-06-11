import numpy as np
from collect_bot_data import collect_bot_data_grid

def calc_win_distance(grid, ground_truths) :
    distances = np.zeros((len(grid), len(grid[0]), len(grid[0][0]), len(grid[0][0][0])))

    for i in range(len(grid)) :
        for j in range(len(grid[0])) :
            for k in range(len(grid[0][0])) :
                for l in range(len(grid[0][0][0])) :
                    distances[i][j][k][l] = abs(grid[i][j][k][l] - ground_truths[i][j])
    return distances


   