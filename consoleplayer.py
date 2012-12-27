from player import Player

class ConsolePlayer(Player):
    def getMove(self):
        return input("> ")
