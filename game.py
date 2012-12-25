from board import Board
from msexceptions import GotMineError

class Game:
    def __init__(self, x=10, y=10):
        self.board = Board(x, y)

    def play(self):
        line = ""
        while line != "quit":
            self.board.print(showAll=True)
            try:
                line = input("> ")
            except EOFError:
                print()
                break

            try:
                self.board.pick(1,1)
            except GotMineError:
                print("Got a mine!")
                self.board.print(showAll=True)
                break
