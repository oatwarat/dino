from turtle import Turtle, Screen

ground_lv = -115
gravity = -10
screen = Screen()


class Dinosaur:

    def __init__(self):
        self.dina = Turtle()
        self.dy = 0

    def lil_dino(self):
        self.dina.hideturtle()
        self.dina.left(90)
        screen.addshape('dinofly.gif')
        self.dina.shape("dinofly.gif")
        self.dina.shapesize(1)
        self.dina.height = 200
        self.dina.width = 200
        self.dina.color("green")
        self.dina.penup()
        self.dina.goto(-400, ground_lv + self.dina.height / 2 - 30)
        self.dina.showturtle()

    def update(self):
        print('jumping!')
        self.dy = 50

    def gravity(self):
        self.dy += gravity
        y = self.dina.ycor()
        y += self.dy
        self.dina.sety(y)
        screen.update()
        #if self.dina.ycor() < ground_lv + 220 / 2:
         #   self.dina.sety(ground_lv + 150 / 2)
          #  self.dina.dy = 1
        #if self.dina.ycor() > (700 - 200 / 2) - 70:
         #   self.dina.sety(250)
          #  self.dina.dy = 1
