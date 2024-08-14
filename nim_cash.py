import numpy as np
from generate_win_table import generate_win_table

def find_win_table_cash(moves, outcomes_found, player1_wins, n, depth, budgets, no_cash_win) :
    if n >= 0 and outcomes_found[n] :
        return
    elif n <= 0:
        player1_wins[n] = False
        outcomes_found[n] = True
        return
    elif n == 1 and budgets[depth%2] >= 1:
        player1_wins[n] = depth%2
        outcomes_found[n] = True
        return

    else :
        #print("HERE", n, player1_wins[n], depth)
        for move in moves :
            if n - move >= 0 and budgets[depth % 2] >= move:
                if not outcomes_found[n - move]:
                    budgets[depth % 2] -= move
                    find_win_table_cash(moves, outcomes_found, player1_wins, n - move, depth + 1, budgets, no_cash_win)
                # if no_cash_win[n - move] == 2 :
                #     player1_wins[n] = True
                #     outcomes_found[n] = True
                    return
    player1_wins[n] = False
    return

def generate_win_table_cash(moves, n, budgets) :
    outcomes_found = np.full(n + 1, False)
    player1_wins = np.full(n + 1, False)
    
    player1_cash = budgets[0]
    player2_cash = budgets[1]

    no_cash_win = generate_win_table(moves, n)
    if player1_cash >= n and player2_cash >= n:
        return no_cash_win
    
    cash_win = np.full(n+1, False)
    for i in range(0, min(player1_cash, player2_cash)+1):
        cash_win = no_cash_win[i] == 1
        outcomes_found[i] = True
    
    for i in range(player1_cash + player2_cash, n+1) :
        cash_win[i] = player1_cash > player2_cash
        outcomes_found[i] = True
    
    for i in range(min(player1_cash, player2_cash) * 2, n+1):
        cash_win = player1_cash > player2_cash
        outcomes_found[i] = True


    find_win_table_cash(moves, outcomes_found, cash_win, n, 0, budgets, no_cash_win)

    win_table = np.where(player1_wins, 1, 2)
    return win_table