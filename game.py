import pyglet
from pyglet.window import key
from agent import Agent


class Game(pyglet.window.Window):
    is_left_pressed = False
    is_right_pressed = False

    center_circle = None
    agent = None

    def on_draw(self):
        self.clear()
        self.agent.draw()

    def move(self, dt):
        if self.is_left_pressed:
            self.agent.tern_left(dt)
        if self.is_right_pressed:
            self.agent.tern_right(dt)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.is_left_pressed = True
        if symbol == key.RIGHT:
            self.is_right_pressed = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.is_left_pressed = False
        if symbol == key.RIGHT:
            self.is_right_pressed = False

    def __init__(self):
        super(Game, self).__init__(width=400, height=822, resizable=False)
        self.center_circle = [self.width // 2, self.width // 2 + 10]
        self.agent = Agent(self)
        pyglet.clock.schedule(self.move)
