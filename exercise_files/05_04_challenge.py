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
        if round(point[0]) >= self._x:
            print("out of bounds on the X wall - RIGHT")
            # return(round(point[0]) >= self._x)
            return "RIGHT"
        elif round(point[0]) < 0:
            print("out of bounds with the X axis - LEFT")
            # return round(point[0]) < 0
            return "LEFT"
        elif round(point[1]) >= self._y:
            print("out of bounds with the Y wall - DOWN")
            # return round(point[1]) >= self._y
            return "DOWN"
        elif round(point[1]) < 0:
            print("out of bound with the Y axis - TOP")
            # return round(point[1]) < 0
            return "TOP"
        elif (round(point[0]) >= self._x) and (round(point[1]) < 0):
            print("top, right")
        elif (round(point[0]) < 0) and (round(point[1]) < 0):
            print("smth")
        elif (round(point[1]) >= self._y) and (round(point[1]) < 0):
            print("tadaa")
        elif (round(point[0]) >= self._x) and (round(point[1]) >= self._y):
            print("sup")

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
        self.framerate = 0.20
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def getDegrees(self):
        return self.direction

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

    def forward(self, distance):
        for _ in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            # rounded_pos = [round(pos[0]), round(pos[1])]
            if 0 <= pos[0] < self.canvas._x and 0 <= pos[1] < self.canvas._y:
                self.draw(pos)
                self.pos = pos 
            else:
                # print(f"Out of bounds at pos: {pos}")
                # if self.canvas.hitsWall(pos) == "LEFT":
                #     self.direction = [-self.direction[0], self.direction[1]]
                #     self.draw(pos)
                # elif self.canvas.hitsWall(pos) == "RIGHT":
                #     self.direction = [-self.direction[0], self.direction[1]]
                #     self.draw(pos)
                # elif self.canvas.hitsWall(pos) == "UP":
                #     self.direction = [self.direction[0], -self.direction[1]]
                #     self.draw(pos)
                # elif self.canvas.hitsWall(pos) == "DOWN":
                #     self.direction = [self.direction[1], -self.direction[1]]
                #     self.draw(pos)
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
                self.direction = [-self.direction[0], -self.direction[1]]  # Reverse direction
                self.draw(pos)
                self.pos = pos
                    
        

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

canvas = Canvas(15, 15)
scribe = TerminalScribe(canvas)
scribe.pos = [5, 5]
scribe.setDegrees(30)
scribe.forward(40)
print()
# scribe.getDegrees()
print()
print(scribe.getDegrees())

# TODO scribes should bounce off walls
# TODO modify the forward function to take on a distance, which will move the scribe forward that number of times. 
# TODO one method to bounce is to make the x direction negative on the vertical wall, and y direction negative on the horizontal wall. 
# TODO modify the hitwall method in the canvas to return information about the horizontal or vertical nature of the wall, if one is encountered.
# 