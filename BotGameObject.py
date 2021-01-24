import threading

from Box2D import Box2D

import AggiEngine as ag


class BotGameObject(ag.GameObject):

    def __init__(self, bot):
        ag.GameObject.__init__(self)
        self.bot = bot
        self.botThread = threading.Thread(target=self.bot.update)

    def start(self):
        self.bot.start()
        self.botThread.start()

    def update(self):
        if not self.botThread.is_alive():
            self.body.angle += self.bot.rotation
            self.body : Box2D.b2Body
            # self.body.ApplyForce(self.body.GetLocalVector(self.bot.motion), self.body.worldCenter, True)
            self.body.position += self.body.GetLocalVector(self.bot.motion)
            self.bot.rotation = 0
            self.bot.motion = [0, 0]
            self.botThread = threading.Thread(target=self.bot.update)
            self.botThread.start()
