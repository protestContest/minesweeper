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
            print(self.board.guessNumLeft(), "mines left")
            self.board.print()

            while True:
                try:
                    action = ""
                    line = self.players[0].getMove()
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
                    sys.exit()
                except ValueError:
                    if line == "quit":
                        sys.exit()
                    else:
                        print("Invalid input.")

            try:
                if action == "flag":
                    self.board.flag(x,y)
                elif action == "autopick":
                    self.board.autopick(x,y)
                else:
                    self.board.pick(x,y)
            except GotMineError:
                print("Got a mine!")
                self.board.print(showMines=True)
                break
            except IndexError:
                print(x, ", ", y, " is not on the board.", sep='')

            if self.board.minesLeft == 0:
                playing = False
                print("You won!")

    def addPlayer(self, player):
        player.setBoard(self.board.rows, self.board.cols)
        self.players.append(player)
