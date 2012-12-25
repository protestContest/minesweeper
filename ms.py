#!/usr/bin/python3

from game import Game

if __name__ == "__main__":
    print('''Minesweeper!

This is a clone of minesweeper.  To win, mark all the mines with a flag.
Select a tile by entering the row and column number, separated by a single
space, like this:

> 4 7

Currently there is no mechanism to flag a mine.
To quit, type "quit"
''')
    g = Game()
    g.play()
