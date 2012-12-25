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
