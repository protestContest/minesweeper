from cell import Cell
import random
from msexceptions import GotMineError

class Board:
    def __init__(self, x=10, y=10, r=0.1):
        if x < 0 or y < 0:
            raise Exception("Invalid board size.")
        if r < 0 or r > 1:
            raise Exception("Invalid difficulty rating.")

        self.grid = [0] * x
        self.rows = x
        self.cols = y
        self.minesLeft = 0
        self.numMines = 0
        self.numFlagged = 0
        for i in range(x):
            self.grid[i] = [0] * y
            for j in range(y):
                if random.random() < r:
                    self.minesLeft += 1
                    self.numMines += 1
                    self.grid[i][j] = Cell(True)
                else:
                    self.grid[i][j] = Cell(False)
        
        for i in range(x):
            for j in range(y):
                curVal = 0
                for di in range(i-1, i+2):
                    for dj in range(j-1, j+2):
                        if di < 0 or di >= x or dj < 0 or dj >= y:
                            continue
                        if self.grid[di][dj].isMine:
                            curVal += 1
                self.grid[i][j].value = curVal

    def print(self, showMines=False, showAll=False):
        numColWidth = len(str(self.rows))
        print(" " * numColWidth, end='')
        for i in range(0, self.cols, 3):
            print(i, " "*(2*3 - len(str(i))), end='', sep='')
        print()

        for i in range(self.rows):
            if i%3 == 0:
                print(i, " "*(numColWidth - len(str(i))), end='', sep='')
            else:
                print(" " * numColWidth, end='')
            for j in range(self.cols):
                if self.grid[i][j].isVisible or showAll \
                        or (showMines and self.grid[i][j].isMine):
                    self.grid[i][j].print(revealed=True)
                else:
                    self.grid[i][j].print()
                print(" ", end='')
            print()

    def pick(self, x, y):
        if self.grid[x][y].isFlagged:
            return
        elif self.grid[x][y].isMine:
            raise GotMineError()
        elif self.grid[x][y].isVisible:
            return
        else:
            self.grid[x][y].isVisible = True
            if self.grid[x][y].value == 0:
                self.autopick(x, y)

    def autopick(self, x, y):
        if not self.grid[x][y].isVisible:
            return
        for di in range(x-1, x+2):
            for dj in range(y-1, y+2):
                if di < 0 or di >= self.rows \
                        or dj < 0 or dj >= self.cols \
                        or (di == x and dj == y):
                    continue
                self.pick(di, dj)

    def flag(self, x, y):
        if not self.grid[x][y].isVisible:
            if self.grid[x][y].isFlagged:
                if self.grid[x][y].isMine:
                    self.minesLeft += 1
                self.numFlagged -= 1
                self.grid[x][y].isFlagged = False
            else:
                if self.grid[x][y].isMine:
                    self.minesLeft -= 1
                self.numFlagged += 1
                self.grid[x][y].isFlagged = True

    def guessNumLeft(self):
        return self.numMines - self.numFlagged
