import os
import time
from termcolor import colored

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.8
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    # Created a few methods to help draw the diamond shape
    def down_right(self):
        pos = [self.pos[0]+1, self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
    def down_left(self):
        pos = [self.pos[0]-1, self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def up_left(self):
        pos = [self.pos[0]-1, self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
    
    def up_right(self):
        pos = [self.pos[0]+1, self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    # Created a function to modify the initial position of the mark - necessary for the diamond shape

    def set_start(self, width, depth):
        self.pos = [width, depth]

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

    # Defined the function that makes squares directly within the TerminalScribe class. this way, any object of the class can use it.

    def make_square(self, size):
        for i in range(size-1):
            self.right()
        for i in range(size -1):
            self.down()
        for i in range(size-1):
            self.left()
        for i in range(size-1):
            self.up()

# Create a new Canvas instance that is 30 units wide by 30 units tall 
canvas = Canvas(30, 30)

# Create a new scribe and give it the Canvas object
scribe = TerminalScribe(canvas)

# Draw a small square
# scribe.right()
# scribe.right()
# scribe.right()
# scribe.down()
# scribe.down()
# scribe.down()
# scribe.left()
# scribe.left()
# scribe.left()
# scribe.up()
# scribe.up()
# scribe.up()
# create a function that draws a square. 
# be able to pass in the size of the square as an arguement
# TODO Try and draw other shapes
# TODO draw_square method on the terminal scribe class itself

def draw_square(size):
    
    for i in range(size-1):
        scribe.right()
    for i in range(size -1):
        scribe.down()
    for i in range(size-1):
        scribe.left()
    for i in range(size-1):
        scribe.up()
# diamond

def draw_diamond(hight, scrb):
    #try and make a function to draw a romb shape

    if hight % 2 ==0:
        print("Error, the hight must be an odd number.")
        return
    else:
        top_hight = int(hight / 2)
        bot_hight = top_hight
    
    scrb.set_start(hight+1, 0)
    for i in range(top_hight):
        scribe.down_right()
    for i in range(bot_hight):
        scribe.down_left()
    for i in range(bot_hight):
        scribe.up_left()
    for i in range(top_hight):
        scribe.up_right()
    



# scribe.set_start(8,3)
# draw_square(6)
draw_diamond(11, scribe)
# scribe.make_square(4)

