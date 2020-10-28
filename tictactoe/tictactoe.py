import random
"""
Tic Tac Toe Player
"""

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
    X goes first in the game, is based on a counter
    """
    counter = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] != EMPTY):
                counter += 1

    if counter % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    turn = player(board)
    result = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.append((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Make a deep copy of the board because we cannot make changes on the board itself. After that return what the action would bein the place
    Throws an exception if you try to make a move that is not allowed
    """
    try:
        copy = []
        for i in range(3):
            cpyHelp = []
            for j in range(3):
                cpyHelp.append(board[i][j])
            copy.append(cpyHelp)
        if (copy[action[0]][action[1]] != EMPTY):
            raise Exception('illegal move')
        turn = player(board)
        if (turn == X):
            copy[action[0]][action[1]] = X
        else :
            copy[action[0]][action[1]] = O
        return copy
    except:
        print('illegal move')

    """
    Returns the winner of the game, if there is one.
    """
def winner(board):
    for i in range(3):
        rows = [board[i][0]]
        col = [board[0][i]]
        for j in range(1, 3):
            if (board[i][j] in rows):
                rows.append(board[i][j])
            if (board[j][i] in col):
                col.append(board[j][i])
        if len(rows) == 3 and rows[0] != EMPTY:
            return rows[0]
        if (len(col) == 3 and col[0] != EMPTY):
            return col[0]
    diag = [board[0][0]]
    for i in range(1, 3):
        if board[i][i] == EMPTY:
            break
        elif (board[i][i] in diag):
            diag.append(board[i][i])
        else:
            break
    if len(diag) == 3 and diag[0] != EMPTY:
        return diag[0]
    oppo = board[0][2] == board[1][1] == board[2][0]
    if oppo:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    choice = winner(board)
    if choice != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    choice = winner(board)
    if choice == None:
        return 0
    elif choice == X:
        return -1
    else:
        return 1

def minimax(board):

    """
    Returns the optimal action for the current player on the board.
    We need to make a treee that gets all of the game states possible that go through
    the possible next stages of the game. the best moves will be if it leads to a win
    """
    #First we need to see if the result of this move is a win
    #We need to go through all of the possible moves on the board to see what is the most optimal play
    #First we need to know who's turn it, so we know who's score we are going to maximize
    #Once we have that, we will call a function that will return a value if the max sizes win or loses

    moves = actions(board)
    if len(moves) == 0:
        print('game over')
        return
    if len(moves) == 9:
        return (random.randrange(3), random.randrange(3))
    max = float('inf')
    min = float('-inf')
    maxMove = 'Replace w best max move'
    turn = player(board)
    for x in moves:
        count = 0
        newBoard = result(board, x)
        verdict = utility(newBoard)
        if (verdict == -1 and turn == X):
            return x
        if verdict == 1 and turn == O:
            return x
        newMove = terminal(newBoard)
        score = miniHelp(newBoard, 0)
        if turn == X:
            if score < max:
                max = score
                maxMove = x
        if turn == O:
            if score >= min:
                min = score
                maxMove = x
        print(score, x)
    if turn == X:
        oppDub = oppoWin(board, X)
    if turn == O:
        oppDub = oppoWin(board, O)
    if (oppDub != None):
        maxMove = oppDub

    return maxMove

"""Iterate through to the ending game state, and returns the value that will accompany min or max. I'm thinking
rn that we should just look for anyting that is > max and < min
BOARD == the board that has been changed, TURN == who's turn it is currently in this game state"""
def miniHelp(board, counter):
    moves = actions(board)
    score = 0
    turn = player(board)
    for x in moves:
        newBoard = result(board, x)
        newMove = terminal(newBoard)
        win = utility(newBoard)
        if (newMove):
            if (win == -1 and turn == X):
                return counter - 100
            elif (win == 1 and turn == X):
                return counter + 100
            elif (win == -1 and turn == O):
                return counter + 100
            elif (win == 1 and turn == O):
                return counter - 100
        else:
            return miniHelp(newBoard, counter + 1)
    return score

"""Returns the move as a tuple that will prevent a win if there is one. If there is none, returns None.
BOARD == curent board state. TURN == current turn"""
def oppoWin(board, turn):
    diag = []
    emptyDiagIndex = []
    for i in range(3):
        rows = []
        col = []
        emptyRowIndex = []
        emptyColINdex = []
        for j in range(3):
            if (board[i][j] != EMPTY):
                rows.append(board[i][j])
            else:
                emptyRowIndex.append(j)
            if (board[j][i] != EMPTY):
                col.append(board[j][i])
            else:
                emptyColINdex.append(j)
        if (board[i][i] != EMPTY):
            diag.append(board[i][i])
        else:
            emptyDiagIndex.append(i)
        if (len(rows) == 2 and rows[0] == rows[1] and turn != rows[0]):
            return (i, emptyRowIndex[0])
        elif (len(col) == 2 and col[0] == col[1] and turn != col[0]):
            return (emptyColINdex[0], i)
    if (len(diag) == 2 and diag[0] == diag[1] and turn != diag[0]):
        return (emptyDiagIndex[0], emptyDiagIndex[0])
    counter = 2
    opp = []
    emptyOppIndex = []
    for i in range(3):
        if (board[i][counter] != EMPTY):
            opp.append(board[i][counter])
        else:
            emptyOppIndex.append((i, counter))
        counter -= 1
    if (len(opp) == 2 and opp[0] == opp[1] and turn != opp[0]):
        return emptyOppIndex[0]
    return None
