import random
from generate_win_table import generate_win_table

def make_move(n, moves, win_table, prob_correct_move) :
    if random.random() < prob_correct_move :
        if win_table[n] == 1 :
            for poss_move in moves :
                if n - poss_move >= 0 and win_table[n - poss_move] == 2 :
                    move = poss_move
                    return move
        else :
            valid_moves = []
            for poss_move in moves :
                if n - poss_move >= 0 :
                    valid_moves.append(poss_move)
            move = random.choice(valid_moves)
            return move
    else :
        valid_moves = []
        for poss_move in moves :
            if n - poss_move >= 0 :
                valid_moves.append(poss_move)
        move = random.choice(valid_moves)
    return move

def play_bot_game(bot1_acc, bot2_acc, moves, n) :
    win_table = generate_win_table(moves, n)
    player1_turn = True

    if n <= 0 :
        return False
    
    while n > 0 :
        if player1_turn :
            move = make_move(n, moves, win_table, bot1_acc)
        else :
            move = make_move(n, moves, win_table, bot2_acc)
        n -= move
        if n == 0 :
            return player1_turn
        player1_turn = not player1_turn
    return player1_turn


# if __name__ == "__main__" :
#     bot1_acc = 1
#     bot2_acc = 1
#     moves = [1, 2, 3]
#     n = 8
#     print(play_bot_game(bot1_acc, bot2_acc, moves, n))
#     print("Done")