import os
import time
from termcolor import colored
import math 


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsVerticalWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitsHorizontalWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    def hitsWall(self, point):
        return self.hitsVerticalWall(point) or self.hitsHorizontalWall(point)

    def getReflection(self, point):
        return [-1 if self.hitsVerticalWall(point) else 1, -1 if self.hitsHorizontalWall(point) else 1]

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
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setPosition(self, pos):
        self.pos = pos

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.direction = [0, -1]
        self.forward(1)

    def down(self):
        self.direction = [0, 1]
        self.forward(1)

    def right(self):
        self.direction = [1, 0]
        self.forward(1)

    def left(self):
        self.direction = [-1, 0]
        self.forward(1)

    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        for i in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if self.canvas.hitsWall(pos):
                self.bounce(pos)
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            self.draw(pos)

    def plotX(self, function):
        for x in range(self.canvas._x):
            pos = [x, function(x)]
            if pos[1] and not self.canvas.hitsWall(pos):
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
        #print(self.pos)
        self.canvas.print()
        time.sleep(self.framerate)


def sine(x):
    return 5*math.sin(x/4) + 15

def cosine(x):
    return 5*math.cos(x/4) + 15

def circleTop(x):
    radius = 10
    center = 20
    if x > center - radius and x < center + radius:
        return center-math.sqrt(radius**2 - (x-center)**2)

def circleBottom(x):
    radius = 10
    center = 20
    if x > center - radius and x < center + radius:
        return center+math.sqrt(radius**2 - (x-center)**2)


canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)
# scribe.drawSquare(5)
# scribe.plotX(sine)
# scribe.plotX(cosine)
# scribe.plotX(circleTop)
# scribe.plotX(circleBottom)
# print(colored('Hello, World!', 'red', 'on_black', ['bold', 'blink']))
# scribe.plotX(circleTop)
# scribe.plotX(circleBottom)

# TODO extend TerminalScribe to add new behaviour
# the classes should use inheritance and 
# have a graphic scribe, a vector scribe, a scribe that does just up, down, left, right. Can make a custom one
# create an interface that does fun things with the termcolor module installed earlier

# the classes should allow users to set parameters such as: position, direction and framerate. 
# these should be set when instantiating the object, and also be able to modify them afterwards(maybe)
class BlueSquareScribe(TerminalScribe):
    def __init__(self, framerate, pos):
        super().__init__(canvas)
        self.framerate = framerate
        self.pos = pos
        self.trail = '.'
        self.mark = '*'

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'blue'))
        #print(self.pos)
        self.canvas.print()
        time.sleep(self.framerate)
    
    def drawSquare(self, size):
        for i in range(size-1):
            pos = [self.pos[0]+1, self.pos[1]]
            self.draw(pos)
        for i in range(size-1):
            pos = [self.pos[0], self.pos[1]+1]
            self.draw(pos)
        for i in range(size-1):
            pos = [self.pos[0]-1, self.pos[1]]
            self.draw(pos)
        for i in range(size-1):
            pos = [self.pos[0], self.pos[1]-1]
            self.draw(pos)

b1 = BlueSquareScribe(0.5, [5,5])
b2 = BlueSquareScribe(0.2, [10,2])
# b1.drawSquare(4)
# b2.drawSquare(5)

class Words(TerminalScribe):
    def __init__(self, framerate, colour, pos):
        super().__init__(canvas)
        self.framerate = framerate
        self.pos = pos
        self.colour = colour
        self.trail = '.'
        self.mark = colored('*', self.colour)
    
    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        time.sleep(self.framerate)

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        self.draw(pos)

class DirectionScribe(TerminalScribe):
    def __init__(self, framerate, trail ='.', mark = '*' ):
        super().__init__(canvas)
        self.framerate = framerate
        self.pos = [0, 0]
        self.mark = mark
        self.trail = trail
        self.direction = [0, 1]
    def bounce(self, pos):
        return super().bounce(pos)
    
    def forward(self, distance):
        return super().forward(distance)
        
    def setDirection(self, degrees):
        return super().setDegrees(degrees)

    def setPosition(self, pos):
        return super().setPosition(pos)
    
    def draw(self, pos):
        return super().draw(pos)

d1 = DirectionScribe(0.8, trail='^', mark="@")
d1.setDirection(300)
d1.setPosition([5,5])
d1.forward(30)
    

w1 = Words(0.1, "green", [8,1])
w2 = Words(0.1, "green", [8,4])
w3 = Words(0.1, "green", [12,1])
w4 = Words(0.1, "green", [13,1])

def first_let(w1, w2, w3):
    for _ in range(8):
        w1.down()
    for _ in range(4):
        w2.right()
    for _ in range(8):
        w3.down()
    
def sec_let(w4):
    for _ in range(8):
        w4.down()

# first_let(w1,w2,w3)
# sec_let(w4)

