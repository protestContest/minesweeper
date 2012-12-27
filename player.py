from board import Board

class Player:
    def __init__(self):
        self.gamestate = Board(0, 0, 0)

    def setBoard(self, x, y):
        self.gamestate = Board(x, y, 0)

    def getMove(self):
        return "0 0"

    def sendState(self, x, y, value):
        self.gamestate[x][y].value = value
