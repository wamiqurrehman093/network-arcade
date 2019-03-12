import arcade
from network import Network

WIDTH = 800
HEIGHT = 600
TITLE = "Networking Client"

BLUE = arcade.color.ALICE_BLUE
RED = arcade.color.RED
GREEN = arcade.color.GREEN

SPEED = 6
SIZE = 60

LEFT = arcade.key.LEFT
RIGHT = arcade.key.RIGHT
UP = arcade.key.UP
DOWN = arcade.key.DOWN

class Player():
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.width = size
        self.height = size
        self.color = color
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.network = None
        self.playerPos = None
        self.player1 = None
        self.player2 = None

    def on_draw(self):
        arcade.start_render()
        self.player1.draw()
        self.player2.draw()

    def setup(self):
        arcade.set_background_color(BLUE)
        self.network = Network()
        self.playerPos = read_pos(self.network.getPos())
        self.player1 = Player(self.playerPos[0], self.playerPos[1], SIZE, GREEN)
        self.player2 = Player(0, 0, SIZE, RED)

    def update(self, delta_time):
        p2Pos = read_pos(self.network.send(make_pos((self.player1.x, self.player1.y))))
        self.player2.x = p2Pos[0]
        self.player2.y = p2Pos[1]
        self.player2.update()
        self.player1.update()

    def on_key_press(self, key, mods):
        if key == LEFT:
            self.player1.change_x = -SPEED
        if key == RIGHT:
            self.player1.change_x = SPEED
        if key == UP:
            self.player1.change_y = SPEED
        if key == DOWN:
            self.player1.change_y = -SPEED

    def on_key_release(self, key, mods):
        if key == LEFT or key == RIGHT:
            self.player1.change_x = 0
        if key == UP or key == DOWN:
            self.player1.change_y = 0

def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def main():
    window = Window(WIDTH, HEIGHT, TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
