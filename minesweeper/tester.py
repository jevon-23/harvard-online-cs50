import minesweeper as ms

def test1():
    b1 = ms.Sentence([1, 2, 3], 1)
    b1.known_mines()
#test1()


def test2():
    ai = ms.MinesweeperAI()
    c1 = (1, 2)
    c2 = (3, 3)
    print(ai.grabCells(c2))
test2()
