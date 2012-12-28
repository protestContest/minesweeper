from player import Player

class ConsolePlayer(Player):
    def getMove(self):
        while True:
            try:
                line = input("> ")
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
                return ["quit", 0, 0]
            except ValueError:
                if line == "quit":
                    return ["quit", 0, 0]
                else:
                    print("Invalid input.")
