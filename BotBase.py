class BotBase:

    def __init__(self):
        self.motion = [0, 0]
        self.rotation = 0

    def start(self):
        pass

    def update(self):
        pass

    def moveForward(self):
        self.motion[0] = 0.1

    def moveBackward(self):
        self.motion[0] = -0.1

    def moveLeft(self):
        self.motion[1] = -0.1

    def moveRight(self):
        self.motion[1] = 0.1

    def rotateLeft(self):
        self.rotation = -0.05

    def rotateRight(self):
        self.rotation = 0.05
