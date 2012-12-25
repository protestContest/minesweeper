from board import Board

class Game:

    def __init__(self, x=10, y=10):
        self.board = Board(x, y)

    def start(self):
        line = input()
        while input != "quit\n":
            line = input()
            self.board.print()
