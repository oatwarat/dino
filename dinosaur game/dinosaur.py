from turtle import Turtle, Screen

ground_lv = -115
gravity = -0.5
screen = Screen()


class Dinosaur:

    def __init__(self):
        self.dina = Turtle()
        self.dy = 0
        self.sety = 0

    def lil_dino(self):
        self.dina.dy = 0
        self.dina.dx = 0
        self.dina.hideturtle()
        self.dina.left(90)
        screen.addshape('dinofly.gif')
        self.dina.shape("dinofly.gif")
        self.dina.shapesize(1)
        self.dina.height = 200
        self.dina.width = 200
        self.dina.color("green")
        self.dina.penup()
        self.dina.goto(-400, ground_lv + self.dina.height / 2-30)
        self.dina.showturtle()

    def update(self):
        print('jumping!')
        self.dina.goto(-400, ground_lv + self.dina.height / 2)
        self.dina.goto(-400, ground_lv)
        print('halo')
        # self.dina.dy += gravity
        # y = self.dina.ycor
        # y += self.dina.dy
        # self.dina.ycor = y
        # if self.dina.ycor < ground_lv + 200 / 2:
        #     self.dina.ycor = ground_lv + 200 / 2
        #     self.dina.dy = 3
        # if self.dina.ycor > (700 - 200 / 2) - 70:
        #     self.dina.ycor = 280
        #     self.dina.dy = 0
