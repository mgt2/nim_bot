import matplotlib.pyplot as plt
import numpy as np
from handle_and_plot_input_and_grid_data import load_data, write_to_file, plot_distances, plot_distances_sequentially
from generate_win_table import generate_win_table

# Assumes distance data is configured like in output_data folder
def configure_distance_trends(distance_data) :
    new_distance_data = np.zeros((len(distance_data['moves']), len(distance_data['0'][0]), len(distance_data['0'][0][0]), len(distance_data['0'])))

    for i in range(len(distance_data['moves'])) :
        for j in range(len(distance_data[str(i)])) :
            for k in range(len(distance_data[str(i)][j])) :
                for l in range(len(distance_data[str(i)][j][k])) :
                    new_distance_data[i][k][l][j] = distance_data[str(i)][j][k][l]
    return new_distance_data

def plot_distance_trends(distance_data, plot_info, moves_list) :
    for ind in plot_info['move_indices'] :
        win_table = generate_win_table(moves_list[ind], plot_info['max_n'])
        for j in range(int(10 * plot_info['min_acc_p1']), int(10 * plot_info['max_acc_p1']) + 1, int(10 * plot_info['acc_increment_p1'])) :
            for k in range(int(10 * plot_info['min_acc_p2']), int(10 * plot_info['max_acc_p2']) + 1, int(10 * plot_info['acc_increment_p2'])) :
                plot_list = []
                x_values = []
                for l in range(plot_info['min_n'], plot_info['max_n'] + 1, plot_info['n_increment']) :
                    if win_table[l] in plot_info['player_wins'] :
                        plot_list.append(distance_data[ind][j][k][l])
                        x_values.append(l)

                plt.plot(x_values, plot_list, label=f"Bot 1: {j/10}, Bot 2: {k/10}")
        plt.xlabel("Number of Sticks")
        plt.ylabel("Average Distance from Perfect Play Outcome")
        plt.title(f"Distance Trends for {moves_list[ind]} with winners {plot_info['player_wins']}")
        plt.legend()
        plt.show()
    return

if __name__ == "__main__" :
    dist_data = load_data("output_data/distances_x_x+1.json")

    new_dist_data = configure_distance_trends(dist_data)

    plot_info = {
        'min_acc_p1' : 0.9,
        'max_acc_p1' : 0.9,
        'acc_increment_p1' : 0.3,
        'min_acc_p2' : 0.9,
        'max_acc_p2' : 0.9,
        'acc_increment_p2' : 0.1,

        'min_n' : 20,
        'max_n' : 100,
        'n_increment' : 1,

        'move_indices' : [0,1,2],
        'player_wins' : [2],
    }

    plot_distance_trends(new_dist_data, plot_info, dist_data['moves'])
