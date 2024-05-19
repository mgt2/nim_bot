import numpy as np
from generate_win_table import generate_win_table
from bot_play import play_bot_game

def run_trials(n, moves, bot1_acc, bot2_acc, num_trials=100) :
    return [play_bot_game(bot1_acc, bot2_acc, moves, n) for _ in range(num_trials)]

def analyze_trials(results) :
    player1_wins = np.sum(results)
    player2_wins = len(results) - player1_wins
    return player1_wins/(player1_wins + player2_wins)

def collect_bot_data_one_game(n, moves, bot_accs, compiled_array, win_table, num_trials_each=100) :
    for i in range(len(bot_accs)) :
        (bot1_acc, bot2_acc) = bot_accs[i]
        results = run_trials(n, moves, bot1_acc, bot2_acc, num_trials_each)
        player1_winrate = analyze_trials(results)
        compiled_array[n][i] = player1_winrate
    return compiled_array

def collect_bot_data_same_moves(max_n, moves, bot_accs, num_trials_each=100) :
    win_table = generate_win_table(moves, max_n)
    ground_truth = np.where(win_table == 1, 1, 0)

    compiled_array = np.zeros(max_n + 1, len(bot_accs))
    for n in range(max_n + 1) :
        compiled_array = collect_bot_data_one_game(n, moves, bot_accs, compiled_array, win_table, num_trials_each)
    return compiled_array, ground_truth

def collect_bot_data(max_n, moves_list, bot_accs, num_trials_each=100) :
    compiled_arrays = []
    ground_truths = []

    for moves_set in moves_list :
        compiled_array, ground_truth = collect_bot_data_same_moves(max_n, moves_set, bot_accs, num_trials_each)
        compiled_arrays.append(compiled_array)
        ground_truths.append(ground_truth)

    return compiled_arrays, ground_truths

def collect_bot_data_grid(max_n, moves_list, min_bot_acc, max_bot_acc, acc_increment, num_trials_each=100) :
    bot_accs = [(acc1, acc2) for acc1 in np.arange(min_bot_acc, max_bot_acc + acc_increment, acc_increment) for acc2 in np.arange(min_bot_acc, max_bot_acc + acc_increment, acc_increment)]
    compiled_arrays, ground_truths = collect_bot_data(max_n, moves_list, bot_accs, num_trials_each)

    grid_array = np.zeros((len(moves_list), max_n + 1, len(np.arange(min_bot_acc, max_bot_acc + acc_increment, acc_increment)), len(np.arange(min_bot_acc, max_bot_acc + acc_increment, acc_increment))))
    for i in range(len(compiled_arrays)) :
        for j in range(max_n + 1) :
            for k in range(len(bot_accs)) :
                (bot1_acc, bot2_acc) = bot_accs[k]
                grid_index_acc1 = int((bot1_acc - min_bot_acc) / acc_increment)
                grid_index_acc2 = int((bot2_acc - min_bot_acc) / acc_increment)
                grid_array[i][j][grid_index_acc1][grid_index_acc2] = compiled_arrays[i][j][k]
    return grid_array, ground_truths
