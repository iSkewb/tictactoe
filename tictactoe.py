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
    xCount = 0
    oCount = 0

    # count the number of X's and O's on the board
    for row in board:
        for item in row:
            if item == X: xCount += 1
            if item == O: oCount += 1
    
    # return the players whose turn it is
    if xCount <= oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    square = boardCopy[action[0]][action[1]]
    if square != EMPTY:
        raise Exception
    elif player(board) == X:
        square = X
    elif player(board) == O:
        square = O
    
    boardCopy[action[0]][action[1]] = square
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check 3 rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # check 3 columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # check 2 diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check if game over because there is a winner
    if winner(board):
        return True

    # check if game over because all spots are filled 
    for row in board:
        for item in row:
            if item == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # check if game is already over
    if terminal(board):
        return None

    bestAction = list(actions(board))[0]
    if player(board) == X:
        for action in actions(board):
            if minValue(result(board, action)) >= minValue(result(board, bestAction)):
                bestAction = action
    elif player(board) == O:
        for action in actions(board):
            if maxValue(result(board, action)) <= maxValue(result(board, bestAction)):
                bestAction = action

    return bestAction
            


def maxValue(board):
    if terminal(board):
        return utility(board)

    value = -1
    for action in actions(board):
        value = max(value, minValue(result(board, action)))
    return value


def minValue(board):
    if terminal(board):
        return utility(board)

    value = 1
    for action in actions(board):
        value = min(value, maxValue(result(board, action)))
    return value