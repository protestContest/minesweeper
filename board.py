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
        for i in range(x):
            self.grid[i] = [0] * y
            for j in range(y):
                if random.random() < r:
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
        for i in range(0, self.cols, 5):
            print(i, " "*(2*5 - len(str(i))), end='', sep='')
        print()

        for i in range(self.rows):
            if i%5 == 0:
                print(i, " "*(numColWidth - len(str(i))), end='', sep='')
            else:
                print(" " * numColWidth, end='')
            for j in range(self.cols):
                if self.grid[i][j].isVisible or showAll \
                        or (showMines and self.grid[i][j].isMine):
                    self.grid[i][j].print()
                else:
                    print("#", end='')
                print(" ", end='')
            print()

    def pick(self, x, y):
        if self.grid[x][y].isMine:
            raise GotMineError()
        elif self.grid[x][y].isVisible:
            return
        else:
            self.grid[x][y].isVisible = True
            if self.grid[x][y].value == 0:
                for di in range(x-1, x+2):
                    for dj in range(y-1, y+2):
                        if di < 0 or di >= self.rows \
                                or dj < 0 or dj >= self.cols \
                                or (di == x and dj == y):
                            continue
                        self.pick(di, dj)
