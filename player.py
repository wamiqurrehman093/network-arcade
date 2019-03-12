from variables import *

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y
