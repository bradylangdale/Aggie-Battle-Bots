from PySide2.QtWidgets import QPushButton, QFileDialog, QLineEdit

import AggiEngine as ag
from Battle import Battle


class Menu(ag.State):

    def __init__(self, ui_path):
        ag.State.__init__(self, ui_path)
        self.label = None
        self.bot1_path = None
        self.bot2_path = None

    def start(self):
        self.window.findChild(QLineEdit, 'bot1Path').cursorPositionChanged.connect(self.setBot1Path)
        self.window.findChild(QLineEdit, 'bot2Path').cursorPositionChanged.connect(self.setBot2Path)
        self.window.findChild(QPushButton).clicked.connect(
            lambda: self.window.stateManager.changeState(Battle('Assets/game.ui', self.bot1_path, self.bot2_path)))

    def setBot1Path(self):
        self.window.findChild(QLineEdit, 'bot1Path').cursorPositionChanged.disconnect(self.setBot1Path)
        self.bot1_path = QFileDialog(self.window).getOpenFileName(caption='Select Bot Script')[0]
        self.window.findChild(QLineEdit, 'bot1Path').setText(self.bot1_path)
        self.window.findChild(QLineEdit, 'bot1Path').cursorPositionChanged.connect(self.setBot1Path)

    def setBot2Path(self):
        self.window.findChild(QLineEdit, 'bot2Path').cursorPositionChanged.disconnect(self.setBot2Path)
        self.bot2_path = QFileDialog(self.window).getOpenFileName(caption='Select Bot Script')[0]
        self.window.findChild(QLineEdit, 'bot2Path').setText(self.bot2_path)
        self.window.findChild(QLineEdit, 'bot2Path').cursorPositionChanged.connect(self.setBot2Path)


state = Menu('Assets/menu.ui')
app = ag.Application(state, screenFps=60, fixedFps=60)  # starts the application at 60 hz screen, and 60 hz physics
app.run()
