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
                    args = line.split(" ")
                    if args[0] == "f":
                        x,y = [int(i) for i in args[1:]]
                        action = "flag"
                    elif args[0] == "a":
                        x,y = [int(i) for i in args[1:]]
                        action = "autopick"
                    else:
                        x,y = [int(i) for i in args]
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
            elif action == "autopick":
                self.board.autopick(x,y)
            else:
                try:
                    self.board.pick(x,y)
                except GotMineError:
                    print("Got a mine!")
                    self.board.print(showMines=True)
                    break

