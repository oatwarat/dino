import turtle
from random import randint

screen = turtle.Screen()


class Obstacles:
    random_x = randint(-200, 1000)
    random_y = randint(100, 300)

    def __init__(self, pos):
        self.pos = pos

    def small_cactus(self, cactus):
        cactus.penup()
        cactus.speed(0)
        cactus.goto(self.pos.x, self.pos.y)
        cactus.pendown()
        screen.addshape('cactus.gif')
        cactus.shape("cactus.gif")
        cactus.shapesize(1)
        cactus.height = 150
        cactus.width = 150
        cactus.color("green")

    def update(self, dt):
        self.pos.x -= dt
