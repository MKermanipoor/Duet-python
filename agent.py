import pyglet
import numpy as np


class Agent:
    blue_ball_angle = 0.0
    angular_velocity = np.pi

    def __init__(self, game):
        self.center_circle = [game.width // 2, game.width // 4 + game.width * .08 + 15]
        self.center_radius = game.width // 4

        blue_circle = pyglet.resource.image('resource/images/blue-circle.png')
        blue_circle.width = game.width * .08
        blue_circle.height = game.width * .08
        blue_circle.anchor_x = blue_circle.width // 2
        blue_circle.anchor_y = blue_circle.height // 2
        self.blue_ball_sprite = pyglet.sprite.Sprite(blue_circle)

        red_circle = pyglet.resource.image('resource/images/red-circle.png')
        red_circle.width = game.width * .08
        red_circle.height = game.width * .08
        red_circle.anchor_x = red_circle.width // 2
        red_circle.anchor_y = red_circle.height // 2
        self.red_ball_sprite = pyglet.sprite.Sprite(red_circle)

    def __get_ball_position(self, angel):
        x = self.center_circle[0] + self.center_radius * np.cos(angel)
        y = self.center_circle[1] + self.center_radius * np.sin(angel)
        return [x, y]

    def draw(self):
        blue_ball_position = self.__get_ball_position(self.blue_ball_angle)
        self.blue_ball_sprite.x = blue_ball_position[0]
        self.blue_ball_sprite.y = blue_ball_position[1]

        red_ball_position = self.__get_ball_position(self.blue_ball_angle + np.pi)
        self.red_ball_sprite.x = red_ball_position[0]
        self.red_ball_sprite.y = red_ball_position[1]

        self.blue_ball_sprite.draw()
        self.red_ball_sprite.draw()

    def tern_left(self, dt):
        self.blue_ball_angle += self.angular_velocity * dt
        if self.blue_ball_angle > 2 * np.pi:
            self.blue_ball_angle -= 2 * np.pi

    def tern_right(self, dt):
        self.blue_ball_angle -= self.angular_velocity * dt
        if self.blue_ball_angle < 0:
            self.blue_ball_angle += 2 * np.pi
