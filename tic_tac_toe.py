import math

def initialize_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def play_game():
    board = initialize_board()
    while True:
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win great victry master1!")
            break
        if is_board_full(board):
            print("Try again Son its a tie!")
            break

        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Make a proper move manhh. Try again.")
            continue
        board[move] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win great victry master!")
            break
        if is_board_full(board):
            print_board(board)
            print("ITry again Son its a tie")
            break

        move = ai_move(board)
        board[move] = 'O'
        if check_winner(board, 'O'):
            print_board(board)
            print("You loose shame on you try again")
            break
        if is_board_full(board):
            print_board(board)
            print("Try again Son its a tie!")
            break

play_game()