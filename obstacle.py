import pyglet


class ObstacleAlignment:
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class Obstacle:

    def __init__(self, game, alignment):
        self.alignment = alignment
        self.velocity = 100
        self.alive = True

        obstacle_image = pyglet.resource.image('resource/images/obstacle.png')
        obstacle_image.width = game.width * .55
        obstacle_image.height = game.width * .1
        obstacle_image.anchor_x = obstacle_image.width // 2
        obstacle_image.anchor_y = obstacle_image.height // 2
        self.sprite = pyglet.sprite.Sprite(obstacle_image, y=game.height + obstacle_image.height // 2,
                                           x=obstacle_image.width // 2)

    def touch(self):
        obstacle_image = pyglet.resource.image('resource/images/obstacle_red.png')
        obstacle_image.width = self.get_width()
        obstacle_image.height = self.get_height()
        obstacle_image.anchor_x = obstacle_image.width // 2
        obstacle_image.anchor_y = obstacle_image.height // 2
        self.sprite = pyglet.sprite.Sprite(obstacle_image, y=self.get_y(), x=self.get_x())

    @staticmethod
    def make_random_obstacle(game):
        return Obstacle(game, ObstacleAlignment.LEFT)

    def draw(self):
        self.sprite.draw()

    def move(self, dt):
        self.sprite.y -= self.velocity * dt
        if self.sprite.y < -self.sprite.height - 10:
            self.alive = False

    def get_y(self):
        return self.sprite.y

    def get_height(self):
        return self.sprite.height

    def get_x(self):
        return self.sprite.x

    def get_width(self):
        return self.sprite.width
