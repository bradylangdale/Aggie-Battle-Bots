from BotBase import BotBase
import time
import random


class BotExample(BotBase):

    def __init__(self):
        BotBase.__init__(self)

    def update(self):
        self.moveForward()
        self.rotateLeft()
