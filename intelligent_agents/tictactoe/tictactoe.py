"""
  Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError
    xs = 0
    os = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xs += 1
            elif board[i][j] == O:
                os += 1
    
    # if empty > xs and empty > os:
    #     return X    # new game
    # elif xs > os:
    #     return O    # more Xs means that the next move is for O
    # elif os > xs:
    #     return X 
    # else:
    #     return X 
    if xs > os:
        return O
    else:
        return X    # return X for first game, for terminal board and when O just played


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    possible_actions = {}
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    i = action[0]
    j = action[1]
    
    if i > 2 or j > 2 or i < 0 or j < 0:
        raise ValueError("Invalid action")

    player = player(board)

    new_board = copy.deepcopy(board)
    new_board[i][j] = player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    
    # fijo fila y recorro columnas
    for i in range(3):
        player = board[i][0]
        if player is EMPTY: continue 
        if board[i][1] == player and board[i][2] == player:
            return player
        
    # fijo columna y recorro filas
    for j in range(3):
        player = board[0][j]
        if player is EMPTY: continue 
        if board[1][j] == player and board[2][j] == player:
            return player    

    # miro diagonal 1
    player = board[0][0]
    if player is not EMPTY and board[1][1] == player and board[2][2] == player:
        return player
    
    # miro diagonal 2
    player = board[0][2]
    if player is not EMPTY and board[1][1] == player and board[2][0] == player:
        print("Gana", player, "en la diagonal secundaria")

    
    return None # nobody wins


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    return winner(board) or not actions(board)    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    winner = winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board):
        return None 
    
    player = player(board)

