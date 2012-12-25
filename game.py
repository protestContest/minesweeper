from board import Board

class Game:

    def __init__(self, x=10, y=10):
        self.board = Board(x, y)

    def play(self):
        line = ""
        while line != "quit":
            self.board.print()
            try:
                line = input("> ")
            except EOFError:
                break
