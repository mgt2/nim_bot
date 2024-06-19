import matplotlib.pyplot as plt
import numpy as np
import json
from generate_win_table import generate_win_table
from collect_bot_data import collect_bot_data_grid
from distance import calc_win_distance

def plot_distances_sequentially(distances, moves_list) :
    for i in range(len(distances)) :
        for j in range(len(distances[i])) :
            plt.imshow(distances[i][j], cmap='hot', interpolation='nearest')
            plt.title("Win Rate Distance for " + str(moves_list[i]) + " starting with " + str(j) + " sticks")
            plt.xlabel("Bot 2 Accuracy (0-10)")
            plt.ylabel("Bot 1 Accuracy (0-10)")
            for k in range(len(distances[i][j])):
                for l in range(len(distances[i][j][k])):
                    plt.text(l, k, "{:.2f}".format(distances[i][j][k][l]), ha='center', va='center', color='green')

            # Add a colorbar to show the mapping of values to colors
            plt.colorbar()

            plt.show()
    return

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

def load_data(data_file_path) :
    with open(data_file_path, 'r') as f :
        data = json.load(f)
    return data

def write_to_file(data, file_path="input_data/data.json") :
    json_data = json.dumps(data, indent=4) # indent for human-readable formatting
    with open(file_path, "w") as json_file:
        json_file.write(json_data)
    
    print("Data has been written to", file_path)
    return
#------------------------------------------------------------
# DISTANCE DATA STORING CODE

if __name__ == "__main__" :
    data = load_data("input_data/x_x+1_x+2.json")

    ground_truths = []
    for move in data['moves'] :
        ground_truths.append(generate_win_table(move, data['n']))
    data['ground_truths'] = ground_truths

    grid, perfect_play = collect_bot_data_grid(data['n'], data['moves'], 0, 1, 0.1)
    data['grid'] = grid

    win_rate_distances = calc_win_distance(grid, perfect_play)

    output_data = {}
    output_data['moves'] = data['moves']
    for i in range(len(win_rate_distances)) :
        output_data[str(i)] = win_rate_distances[i].tolist()
    write_to_file(output_data, "output_data/distances_x_x+1_x+2.json")

#------------------------------------------------------------
# DATA GENERATION CODE

# if __name__ == "__main__" :
#     moves = []
#     accs = []
#     num_sticks = 100
#     data = {}

#     for i in range(2, 24) :
#         moves.append([1, i, i+3])
    
#     for i in range(0, 11) :
#         for j in range(0, 11) :
#             accs.append((i/10, j/10))
    
#     data['moves'] = moves
#     data['accs'] = accs
#     data['n'] = num_sticks

#     write_to_file(data, "input_data/x_x+3.json")
#------------------------------------------------------------
# SIMPLE PLOT TESTING CODE

# if __name__ == "__main__" :
#     n = 10
#     moves = [[1, 2, 3]]
#     min_acc = 0
#     max_acc = 1

#     grid, truth = collect_bot_data_grid(n, moves, min_acc, max_acc, 0.1)
#     distances = calc_win_distance(grid, truth)
#     plot_distances(distances, moves)
   