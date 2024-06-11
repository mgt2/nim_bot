import matplotlib.pyplot as plt
import numpy as np
import json
from generate_win_table import generate_win_table
from collect_bot_data import collect_bot_data_grid
from distance import calc_win_distance

def plot_distances(distances, moves_list):
    num_rows = len(distances)
    num_cols = len(distances[0])

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

    for i in range(num_rows):
        for j in range(num_cols):
            axes[i, j].imshow(distances[i][j], cmap='hot', interpolation='nearest')
            if j == 0:
                axes[i, j].set_title(str(moves_list[i]) + ", 0 sticks")
            else:
                axes[i, j].set_title(str(j) + " sticks")
            # axes[i, j].set_xlabel("Bot 2 Accuracy (0-10)")
            # axes[i, j].set_ylabel("Bot 1 Accuracy (0-10)")
            # for k in range(len(distances[i][j])):
            #     for l in range(len(distances[i][j][k])):
            #         axes[i, j].text(l, k, f"{distances[i][j][k][l]:.2f}", ha='center', va='center', color='green')

            # Add a colorbar to show the mapping of values to colors
    #fig.colorbar(axes[i, j].imshow(distances[i][j], cmap='hot', interpolation='nearest'), ax=axes[i, j])

    plt.show()


if __name__ == "__main__" :
    n = 100
    moves = [[1, 2, 3], [1,3,4]]
    min_acc = 0
    max_acc = 1

    grid, truth = collect_bot_data_grid(n, moves, min_acc, max_acc, 0.1)
    distances = calc_win_distance(grid, truth)

    distances = distances[:, 90:, :, :]
    plot_distances(distances, moves)