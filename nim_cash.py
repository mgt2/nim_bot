import numpy as np
from generate_win_table import generate_win_table

def find_win_table_cash(moves, outcomes_found, player1_wins, n, depth, budgets, no_cash_win) :
    if n <= 0:
        return False
    elif n == 1 and budgets[depth%2] >= 1:
        return depth % 2 == 0
    
    elif budgets[depth%2] <= 0 :
        return depth % 2 == 1

    else :
        #print("HERE", n, player1_wins[n], depth)
        for move in moves :
            if n - move >= 0 and budgets[depth % 2] >= move:
                budget_copy = [budgets[0], budgets[1]]
                budget_copy[depth % 2] -= move
                result = find_win_table_cash(moves, outcomes_found, player1_wins, n - move, depth + 1, budget_copy, no_cash_win)
                if result == depth % 2:
                    return depth % 2

    return (depth + 1) % 2

def generate_win_table_cash(moves, n, budgets) :
    outcomes_found = np.full(n + 1, False)
    player1_wins = np.full(n + 1, False)
    
    player1_cash = budgets[0]
    player2_cash = budgets[1]

    no_cash_win = generate_win_table(moves, n)
    if player1_cash >= n and player2_cash >= n:
        return no_cash_win
    
    cash_win = np.full(n+1, False)

    for i in range(0, min(player1_cash, player2_cash)+2):
        cash_win[i] = no_cash_win[i] == 1
    
    for i in range(min(player1_cash, player2_cash) * 2 + 1, n+1):
        cash_win[i] = player1_cash > player2_cash

    for i in range(min(player1_cash, player2_cash)+2, min(min(player1_cash, player2_cash) * 2 + 1, n+1)):
        cash_win[i] = find_win_table_cash(moves, outcomes_found, cash_win, n, 0, budgets, no_cash_win)

    win_table = np.where(cash_win, 1, 2)
    return win_table


if __name__ == "__main__" :
    moves = input("Enter the moves, separated by commas: ").split(",")
    budgets = input("Enter the budgets, separated by commas: ").split(",")

    # Convert the moves and budgets to integers
    moves = [int(move) for move in moves]
    budgets = [int(budget) for budget in budgets]
    
    n = 10
    win_table = generate_win_table_cash(moves, n, budgets)
    print(win_table)
    print("Done")