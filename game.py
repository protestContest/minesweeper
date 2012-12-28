from board import Board 
from msexceptions import GotMineError
from player import Player
import sys

class Game:
    def __init__(self, x=10, y=10, mines=10):
        self.board = Board(x, y, mines)
        self.players = []

    def play(self):
        if self.players == []:
            print("No players")
            return

        line = ""
        action = ""
        playing = True
        while playing:
            for player in self.players:
                player.printState()

                move = player.getMove()
                action = move[0]
                if action == "quit":
                    sys.exit()
                else:
                    x, y = move[1:3]

                try:
                    if x < 0 or y < 0:
                        raise IndexError
                    if action == "quit":
                        sys.exit()
                    elif action == "flag":
                        self.board.flag(x,y)
                        player.sendState([(x, y)], "flag")
                    elif action == "autopick":
                        tiles = self.board.autopick(x,y)
                        player.sendState(tiles)
                    else:
                        tiles = self.board.pick(x,y)
                        player.sendState(tiles)
                except GotMineError:
                    print("Got a mine!")
                    self.board.print(showMines=True)
                    playing = False
                    break
                except IndexError:
                    print("That is not on the board.", sep='')

                if self.board.minesLeft == 0:
                    playing = False
                    print("You won!")
                    self.board.print()

    def addPlayer(self, player):
        player.setBoard(self.board.rows, self.board.cols, self.board.numMines)
        self.players.append(player)
