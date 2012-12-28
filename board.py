from cell import Cell
import random
from msexceptions import GotMineError

class Board:
    def __init__(self, x=10, y=10, mines=10):
        if x < 0 or y < 0:
            raise Exception("Invalid board size.")

        self.grid = [0] * x
        self.rows = x
        self.cols = y
        self.minesLeft = mines
        self.numMines = mines
        self.numFlagged = 0

        for i in range(x):
            self.grid[i] = [0] * y
            for j in range(y):
                self.grid[i][j] = Cell(False)

        for i in range(mines):
            mineX = random.randint(0, x-1)
            mineY = random.randint(0, y-1)
            while self.grid[mineX][mineY].isMine:
                mineX = mineX + 1
                if mineX == x:
                    mineX = 0
                    mineY = mineY + 1
                    if mineY == y:
                        mineY = 0
            self.grid[mineX][mineY].isMine = True 
        
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
        numColWidth = len(str(self.rows)) + 1
        print(" " * numColWidth, end='')
        for i in range(1, self.cols, 3):
            print(i, " "*(2*3 - len(str(i))), end='', sep='')
        print()

        for i in range(self.rows):
            if i%3 == 0:
                print(i+1, " "*(numColWidth - len(str(i))), end='', sep='')
            else:
                print(" "*numColWidth, end='')
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
            return []
        elif self.grid[x][y].isMine:
            raise GotMineError()
        elif self.grid[x][y].isVisible:
            return []
        else:
            self.grid[x][y].isVisible = True
            collector = [(x, y, self.grid[x][y].value)]
            if self.grid[x][y].value == 0:
                collector += self.autopick(x, y)
            return collector

    def autopick(self, x, y):
        if not self.grid[x][y].isVisible:
            return []

        collector = []
        for di in range(x-1, x+2):
            for dj in range(y-1, y+2):
                if di < 0 or di >= self.rows \
                        or dj < 0 or dj >= self.cols \
                        or (di == x and dj == y):
                    continue
                collector += self.pick(di, dj)
        return collector

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
