from board import Board
from msexceptions import GotMineError
import sys

class Game:
    def __init__(self, x=10, y=10):
        self.board = Board(x, y)

    def play(self):
        line = ""
        while line != "quit":
            self.board.print(showAll=True)

            while True:
                try:
                    line = input("> ")
                    x,y = [int(i) for i in line.split(" ")]
                    break
                except EOFError:
                    print()
                    sys.exit()
                except ValueError:
                    print("Invalid input.")


            try:
                self.board.pick(x,y)
            except GotMineError:
                print("Got a mine!")
                self.board.print(showAll=True)
                break
