import matplotlib as plt
import numpy as np
import json
from generate_win_table import generate_win_table
from collect_bot_data import collect_bot_data_grid
from distance import calc_win_distance

def plot_data(distances, moves_list) :
    fig, ax = plt.subplots(1, len(distances))
    for i in range(len(distances)) :
        ax[i].imshow(distances[i])
        ax[i].set_title("Moves: " + str(moves_list[i]))
    plt.show()
    return

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
# DATA PLOTTING CODE

if __name__ == "__main__" :
    data = load_data("input_data/data.json")

    ground_truths = []
    for move in data['moves'] :
        ground_truths.append(generate_win_table(move, data['n']))
    data['ground_truths'] = ground_truths

    grid = collect_bot_data_grid(data['n'], data['moves'], 0, 1, 0.1)
    data['grid'] = grid

    win_rate_distances = calc_win_distance(grid, ground_truths)

    plot_data(win_rate_distances, data['moves'])
#------------------------------------------------------------
# DATA GENERATION CODE

# if __name__ == "__main__" :
#     moves = []
#     accs = []
#     num_sticks = 100
#     data = {}

#     for i in range(3, 24) :
#         moves.append([1, i, i+1])
    
#     for i in range(0, 11) :
#         for j in range(0, 11) :
#             accs.append((i/10, j/10))
    
#     data['moves'] = moves
#     data['accs'] = accs
#     data['n'] = num_sticks

#     write_to_file(data)
#------------------------------------------------------------
    