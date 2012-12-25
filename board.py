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
                self.grid[i][j] = Cell(random.choice([True, False]))
        
        for i in range(x):
            for j in range(y):
                curVal = 0
                for di in range(i-1, i+1):
                    for dj in range(j-1, j+1):
                        if di < 0 or di >= x or dj < 0 or dj > y:
                            continue
                        if self.grid[di][dj].isMine:
                            curVal += 1
                self.grid[i][j].value = curVal

    def print(self, showAll=False):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j].isVisible or showAll:
                    self.grid[i][j].print()
                else:
                    print("#", end='')
                print(" ", end='')
            print()

    def pick(self, x, y):
        if self.grid[x][y].isMine:
            raise GotMineError()
