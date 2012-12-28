class Cell:
    def __init__(self, isMine = False):
        self.isMine = isMine
        self.isVisible = False
        self.isFlagged = False
        self.value = 0

    def print(self, revealed=False):
        if revealed:
            if self.isMine:
                print("X", end='')
            elif self.value == 0:
                print("-", end='')
            else:
                print(self.value, end='')
        else:
            if self.isFlagged:
                print("\u00A4", end='')
            else:
                print("+", end='')
