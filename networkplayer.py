from player import Player
import socket

class NetworkPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('', 8000))
        self.server.listen(1)

    def getMove(self):
        while True:
            strm, addr = self.server.accept()
            try:
                line = str(strm.recv(32), encoding='utf8')
                args = line.split(" ")
                action = ""
                x, y = 0, 0
                if args[0] == "f":
                    x,y = [int(i)-1 for i in args[1:]]
                    action = "flag"
                elif args[0] == "a":
                    x,y = [int(i)-1 for i in args[1:]]
                    action = "autopick"
                else:
                    x,y = [int(i)-1 for i in args]
                    action = "pick"
                return [action, x, y]
            except EOFError:
                self.server.close()
                return ["quit", 0, 0]
            except ValueError:
                if line == "quit":
                    self.server.close()
                    return ["quit", 0, 0]
                else:
                    print("Invalid input.")
