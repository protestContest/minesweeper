from board import Board
from msexceptions import GotMineError
import sys

class Game:
    def __init__(self, x=10, y=10):
        self.board = Board(x, y)

    def play(self):
        line = ""
        action = ""
        while True:
            self.board.print()

            while True:
                try:
                    action = ""
                    line = input("> ")
                    if line.split(" ")[0] == "f":
                        x,y = [int(i) for i in line.split(" ")[1:]]
                        action = "flag"
                    else:
                        x,y = [int(i) for i in line.split(" ")]
                    break
                except EOFError:
                    print()
                    sys.exit()
                except ValueError:
                    if line == "quit":
                        sys.exit()
                    print("Invalid input.")

            if action == "flag":
                self.board.flag(x,y)
            else:
                try:
                    self.board.pick(x,y)
                except GotMineError:
                    print("Got a mine!")
                    self.board.print(showMines=True)
                    break

