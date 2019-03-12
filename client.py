from variables import *
from player import Player

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.network = None
        self.p1 = None
        self.p2 = None

    def on_draw(self):
        arcade.start_render()
        self.p1.draw()
        self.p2.draw()

    def setup(self):
        arcade.set_background_color(BLUE)
        self.network = Network()
        self.p1 = self.network.getP()

    def update(self, delta_time):
        self.p2 = self.network.send(self.p1)
        self.p1.update()

    def on_key_press(self, key, mods):
        if key == LEFT:
            self.p1.change_x = -SPEED
        if key == RIGHT:
            self.p1.change_x = SPEED
        if key == UP:
            self.p1.change_y = SPEED
        if key == DOWN:
            self.p1.change_y = -SPEED

    def on_key_release(self, key, mods):
        if key == LEFT or key == RIGHT:
            self.p1.change_x = 0
        if key == UP or key == DOWN:
            self.p1.change_y = 0

def main():
    window = Window(WIDTH, HEIGHT, TITLE)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
