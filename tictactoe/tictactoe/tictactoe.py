"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

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
    countx = 0
    counto = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countx += 1
            elif board[i][j] == O:
                counto += 1
    if countx > counto:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a, b = action
    if (player(board) == X):
        board[a][b] = X
    else:
        board[a][b] = O
    return board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if ((board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY)):  # row
            return board[i][0]
        elif ((board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY)):  # column
            return board[0][i]
    if ((board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != EMPTY)):  # diagonal
        return board[0][0]
    elif ((board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != EMPTY)):  # diagonal
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        if ((board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY)):  # row
            return True
        elif ((board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY)):  # column
            return True
    if ((board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != EMPTY)):  # diagonal
        return True
    elif ((board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != EMPTY)):  # diagonal
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win==X:
        return 1
    elif win==O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board)==X:
        acts=actions(board)
        v=-math.inf
        for action in acts:
            minv=min_value(result(deepcopy(board),action))
            if minv>v:
                v=minv
                best_action=action
        return best_action
    else: 
        acts=actions(board)
        v=math.inf
        for action in acts:
            maxv=max_value(result(deepcopy(board),action))
            if maxv<v:
                v=maxv
                best_action=action
        return best_action
def max_value(board):
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0
    acts=actions(board)
    best_action=None
    max= -math.inf
    for action in acts:
        minv=min_value(result(deepcopy(board),action))
        if minv>max:
            max=minv
            best_action=action
    return max

def min_value(board):
    if terminal(board):
        if winner(board)==O:
            return -1
        elif winner(board)==X:
            return 1
        else:
            return 0
    acts =actions(board)
    best_action=None
    min= math.inf
    for action in acts:
        maxv=max_value(result(deepcopy(board),action))
        if maxv<min:
            min=maxv
            best_action=action
    return min
        
    raise NotImplementedError
