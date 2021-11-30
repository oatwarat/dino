import turtle
from random import randint

screen = turtle.Screen()


class Bird:
    random_x = randint(-200, 1000)
    random_y = randint(100, 200)

    def __init__(self, pos):
        self.pos = pos

    def birds(self, bird):
        bird.penup()
        bird.speed(0)
        bird.goto(self.pos.x + self.random_x, self.pos.y + self.random_y)
        bird.pendown()
        screen.addshape('bird.gif')
        bird.shape("bird.gif")
        bird.shapesize(1)
        bird.height = 150
        bird.width = 150
        bird.color("green")

    def update(self, dt):
        self.pos.x -= dt
