#!/usr/bin/python3

from session import Session
from consoleplayer import ConsolePlayer
from networkplayer import NetworkPlayer
import sys
import os

if __name__ == "__main__":
  session = Session()
  print(session.intro())
  session.start(1)

