import os
import time
from termcolor import colored
import math 


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)
# scribe.setDegrees(135)
# for i in range(30):
#     scribe.forward()

# Create a data structure that defines some number of scribes, with instructions for each of those scribes
# and then create a function that takes all of that data and makes the whole thing go
# You may or may not include the canvas definition in the data structure.

# make a list of dictionary objects where each dictionary defines a scribe, plus some instructions to move around.
# remember to include the starting direction for each scribe.
scribes_data = [
    {
        "position" : [0, 0],
        "moves" : ["right", "right", "right","down", "down", "down", "left", "left", "left", "up", "up", "up"],
        "degrees" : 90
    },
    {
        "position" : [5,5],
        "moves" : ["right", "up", "right", "up", "right", "right", "down", "down"],
        "degrees" : 45
    }
]


for scrib in scribes_data:
    scribex = TerminalScribe(canvas)
    scribex.setDegrees(scrib["degrees"])
    scribex.pos = scrib["position"]
    for move in scrib["moves"]:
        if move == "forward":
            scribex.forward()
        elif move == "up":
            scribex.up()
        elif move == "down":
            scribex.down()
        elif move == "right":
            scribex.right()
        elif move == "left":
            scribex.left()
