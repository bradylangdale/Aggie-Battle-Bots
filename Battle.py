import threading
from BotBase import BotBase

from Box2D import b2BodyDef, Box2D, b2FixtureDef, b2PolygonShape
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel
import time
import random
import math

import AggiEngine as ag
from BotGameObject import BotGameObject


class Battle(ag.State):

    def __init__(self, ui_path, bot1, bot2):
        ag.State.__init__(self, ui_path)

        self.bot1 = None
        self.bot2 = None
        self.loadBotFile(bot1, bot2)
        self.label = None

    def start(self):
        self.label = self.window.findChild(QLabel)
        self.label.setVisible(False)
        self.loadMap('Assets/test_map.tmx')
        self.window.gameScreen.cameraScale = 1.3
        self.window.gameScreen.cameraPosition = [-0.75, -0.75]

        self.addBot(self.bot1, -6, -12)
        self.addBot(self.bot2, -18, -12)

    def fixedUpdate(self):
        if self.label.isVisible():
            self.label.setText('Fixed FPS: {:.3f}\nScreen FPS: {:.3f}'.format(
                self.window.fixedFps, self.window.screenFps))

    def keyPressed(self, event):
        if event.key() == Qt.Key_I:
            self.label.setVisible(False if self.label.isVisible() else True)

    def loadBotFile(self, bot1, bot2):
        code = ''
        for line in open(bot1).readlines():
            code += line
        code += 'self.bot1 = Bot1()'
        code = code.replace(code[code.find('class'):code.find(':')], 'class Bot1(BotBase)')
        compiled = compile(code, 'Bot1', 'exec')
        exec(compiled)

        code = ''
        for line in open(bot2).readlines():
            code += line
        code = code.replace(code[code.find('class'):code.find(':')], 'class Bot2(BotBase)')
        code += 'self.bot2 = Bot2()'
        compiled = compile(code, 'Bot2', 'exec')
        exec(compiled)

    def addBot(self, bot, x, y):
        bodyDef = b2BodyDef()
        bodyDef.type = Box2D.b2_dynamicBody
        bodyDef.position = (x, y)

        bodyFixtureDef = b2FixtureDef(shape=b2PolygonShape(box=(0.5, 0.5)))
        bodyFixtureDef.friction = 0.75
        bodyFixtureDef.density = 1

        self.gameObjectHandler.add(BotGameObject(bot), bodyDef, bodyFixtureDef, [1, 1, 1])
