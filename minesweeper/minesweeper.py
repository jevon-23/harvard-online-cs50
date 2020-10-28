import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if self.count == len(self.cells):
            return self.cells

        #raise NotImplementedError

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        #raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell not in self.cells:
            #print("nothing to do here")
            return
        self.cells.remove(cell)
        self.count -= 1
        theMine = Sentence([(cell[0], cell[1])], 8)
        #Update the knowloedge
        #raise NotImplementedError

    def mark_Helper(self, cell, string):
        """ Takes in a cell and checks to see if it is in the sentences' set of cells.
        If STRING checks whether we are working with a mine or a safe, and acts accordingly
        """,

        if cell not in self.cells:
            #print("nothing to do here")
            return False
        if (string == 'mine') and (len(self.cells) == self.count):
            return True
        elif (string == 'safe') and (self.count == 0):
            return True
        else:
            return False

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell not in self.cells:
            return
        elif len(self.cells) <= 1:
            self.count = 0
            return
        else:
            #self.cells.remove(cell)
            theSafe = Sentence([(cell[0], cell[1])], 0)
        #Update the knowledge
        #raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        nearby = self.grabCells(cell)
        #1)
        self.moves_made.add(cell)
        #2)
        self.mark_safe(cell)

        #3)
        theCell = Sentence((cell[0], cell[1]), count)
        self.knowledge.append(theCell)
        if count != 0:
            self.knowledge.append(Sentence(nearby, count))
        #4)
        isSafe, isMine = count == 0, count == 8

        if isSafe or isMine:
            for x in nearby:
                if isSafe and (x not in self.safes):
                    sen = Sentence([], count)
                    sen.cells.add((x[0], x[1]))
                    self.knowledge.append(sen)
                    self.mark_safe(x)
                elif isMine and (x not in self.mines):
                    sen = Sentence([], 1)
                    sen.cells.add((x[0], x[1]))
                    self.knowledge.append(sen)
                else:
                    self.cornerCase(x)
        '''for x in self.knowledge:
            if x.count == 0:
                for y in x.cells:
                    x.mark_safe(y)
            elif x.count == 8 or x.count == len(x.cells):
                for y in x.cells:
                    x.mark_mine(y)'''
        print('========= knowledge =========')
        for x in self.knowledge:
            print(x)
        print('========= knowledge =========')




    def cornerCase(self, cell):
        for x in self.knowledge:
            if (cell in x.cells):
                if (cell[0] == 0 or cell[0] == self.height) and (cell[1] == 0 or cell[1] == self.width) and (x.count >= 2):
                    self.mark_mine(cell)
                elif (cell[1] == 0 or cell[1] == self.height) or (cell[0] == 0 or cell[0] == self.width) and (x.count >= 5):
                    self.mark_mine(cell)


        #raise NotImplementedError
    def grabCells(self, cell):
        i = cell[0]
        j = cell[1]
        result = []
        #board[i][j]
        if (i + 1 < self.height):
            result.append((i+1, j))
        if (i - 1 >= 0):
            result.append((i - 1, j))
        if (j + 1 < self.width):
            result.append((i, j + 1))
        if (j - 1 > 0):
            result.append((i, j - 1))
        if (i + 1 < self.height) and (j + 1 < self.width):
            result.append((i+1, j+1))
        if (i - 1 >= 0 and j - 1 >= 0):
            result.append((i -1, j-1))
        if (i + 1 < self.height) and (j - 1 >= 0):
            result.append((i + 1, j - 1))
        if (i -1 >= 0) and (j + 1 < self.width):
            result.append((i - 1, j + 1))
        return result

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        theSafe = self.safes.copy()
        if len(self.safes) == 0:
            return None
        while (len(theSafe) != 0):
            theMove = theSafe.pop()
            if (theMove not in self.mines) and (theMove not in self.moves_made):
                return theMove
        return None
        #raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        cellCount = set()
        possible = []
        while (len(cellCount) != self.height * self.width):
            counter = 0
            i = random.randrange(self.height)
            j = random.randrange(self.width)
            cell = (i, j)
            nearby = self.grabCells(cell)
            if cell in cellCount:
                continue
            if (cell not in self.moves_made) and (cell not in self.mines):
                for x in self.knowledge:
                    if cell in x.cells:
                        print('!!!!!!!!!', x.count, 'theCount in knowledge', '!!!!!!!!')
                        counter += x.count
                    for friend in nearby:
                        if (friend in x.cells) and (friend in self.moves_made) and (len(x.cells) == 1):
                            counter += x.count
                print('+++++++++++ RANDOM MOVE +++++++++++++++++')
                print(cell, counter)

                if counter < 4:
                    return cell
                else:
                    possible.append((cell, counter))
            cellCount.add(cell)
        bestMove = (1, 9999)
        for x in possible:
            if x[1] < bestMove[1]:
                bestMove = x
        return bestMove[0]
        #raise NotImplementedError
