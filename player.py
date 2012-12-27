from board import Board

class Player:
    def __init__(self):
        self.gamestate = Board(0, 0, 0)

    def setBoard(self, x, y, mines):
        self.gamestate = Board(x, y, 0)
        self.gamestate.numMines = mines

    def getMove(self):
        return "0 0"

    def sendState(self, tiles):
        for t in tiles:
            self.gamestate.grid[t[0]][t[1]].value = t[2]
            self.gamestate.grid[t[0]][t[1]].isVisible = True

    def printState(self):
       print(self.gamestate.guessNumLeft(), "mines left")
       self.gamestate.print()
