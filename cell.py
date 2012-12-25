class Cell:
    def __init__(self, isMine = False):
        self.isMine = isMine
        self.isVisible = False
        self.value = 0

    def print(self):
        if self.isMine:
            print("*", end='')
        else:
            print(self.value, end='')
