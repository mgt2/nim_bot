import matplotlib as plt
import numpy as np
from distance import calc_win_distance

def plot_data(grid, ground_truths, moves_list) :
    distances = calc_win_distance(grid, ground_truths)
    fig, ax = plt.subplots(1, len(grid))
    for i in range(len(grid)) :
        ax[i].imshow(distances[i])
        ax[i].set_title("Moves: " + str(moves_list[i]))
    plt.show()
    return