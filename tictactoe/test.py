import tictactoe as ttt

""" Where we will be testing our tic tac toe"""
EMPTY = None
X = 'X'
O = 'O'
b1 = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

b2 = [['X', 'X', 'X'],
        ['O', EMPTY, 'O'],
        [EMPTY, 'X', EMPTY]]

b3 = [['X', EMPTY, EMPTY],
        ['O', 'O', 'O'],
        [EMPTY, EMPTY, 'O']]

b4 =     [[X, O, EMPTY],
        [X, X, O],
        [EMPTY, O, X]]

b5 = [[X, EMPTY, O],
        [X, O, EMPTY],
        [O, EMPTY, X]]

b6 = [[O, X, EMPTY],
        [O, X, EMPTY],
        [O, EMPTY, X]]

b7 = [[X, O, O],
        [O, X, X],
        [X, O, O]]

def winningTest():
    global b1, b2, b3, b4, b5, b6, b7
    print('b1, expect None', '0')
    print(ttt.winner(b1))
    print(ttt.utility(b1))
    print(ttt.terminal(b1))
    print('=== b2, x ===', '-1')
    print(ttt.winner(b2))
    print(ttt.utility(b2))
    print(ttt.terminal(b2))
    print('=== b3, o ===', '1')
    print(ttt.winner(b3))
    print(ttt.utility(b3))
    print(ttt.terminal(b3))
    print('=== b4, x ===', '-1')
    print(ttt.winner(b4))
    print(ttt.utility(b4))
    print(ttt.terminal(b4))
    print('=== b5, o ===', '1')
    print(ttt.winner(b5))
    print(ttt.utility(b5))
    print(ttt.terminal(b5))
    print('=== b6, x ===', '-1')
    print(ttt.winner(b6))
    print(ttt.utility(b6))
    print(ttt.terminal(b6))
    print(ttt.actions(b6))
    print('=== b7, none ===', '0')
    print(ttt.winner(b7))
    print(ttt.utility(b7))
    print(ttt.terminal(b7))
    print(ttt.actions(b7))
#winningTest()
b8 = [[EMPTY, EMPTY, X],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, X]]

def quicky():
    print(ttt.utility(ttt.result(b8, (1, 2))))
    print(ttt.result(b8, (1, 2)))
quicky()
def minimaxTest():
    print(ttt.minimax(b1))
#minimaxTest()



nb1 = [[O, O, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
nb2 = [[EMPTY, O, EMPTY],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
nb3 = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, O]]
nb4 = [[EMPTY, EMPTY, O],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

nb5 = [[O, EMPTY, X],
        [EMPTY, X, O],
        [EMPTY, EMPTY, O]]
def oppoTest():
    print(ttt.oppoWin(nb1, X))
    print(ttt.oppoWin(nb2, X))
    print(ttt.oppoWin(nb3, X))
    print(ttt.oppoWin(nb4, X))
    print(ttt.oppoWin(nb5, X))

#oppoTest()
