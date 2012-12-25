from cell import Cell

class Board:

    def __init__(self, x=10, y=10):
        self.grid = [0] * x
        self.rows = x
        self.cols = y
        for i in range(x):
            self.grid[i] = [0] * y
            for j in range(y):
                self.grid[i][j] = Cell()

    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j].isVisible:
                    print(self.grid[i][j].value, end='')
                else:
                    print("#", end='')
                print(" ", end='')
            print()
