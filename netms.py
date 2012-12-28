#!/usr/bin/python3

import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8000))
    while True:
        try:
            line = input("> ")
        except EOFError:
            s.send(b"quit")
            s.close()
            break
        s.send(line.encode())
        if line == "quit":
            s.close()
            break
