import pyglet
from pyglet.window import key
from agent import Agent
from obstacle import Obstacle


class Game(pyglet.window.Window):

    def on_draw(self):
        self.clear()
        self.agent.draw()

        for obstacle in self.obstacles:
            obstacle.draw()

    def create_obstacle(self):
        if len(self.obstacles) > 0:
            if self.height - self.obstacles[-1].get_y() - self.obstacles[-1].get_height() // 2 > self.width * 0.38:
                self.obstacles.append(Obstacle.make_random_obstacle(self))
        else:
            self.obstacles.append(Obstacle.make_random_obstacle(self))

    def remove_die_obstacle(self):
        if len(self.obstacles) > 0:
            if not self.obstacles[0].alive:
                self.obstacles = self.obstacles[1:]

    def iterate(self, dt):
        self.create_obstacle()
        self.remove_die_obstacle()

        for obstacle in self.obstacles:
            obstacle.move(dt)

        if self.is_left_pressed:
            self.agent.tern_left(dt)
        if self.is_right_pressed:
            self.agent.tern_right(dt)

        for obstacle in self.obstacles:
            if self.agent.is_intersects(obstacle):
                obstacle.touch()

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

        self.is_left_pressed = False
        self.is_right_pressed = False

        self.agent = Agent(self)
        self.obstacles = []

        pyglet.clock.schedule(self.iterate)
