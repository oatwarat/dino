from turtle import Turtle, Screen
from texts import Texts
from dinosaur import Dinosaur
from bird import Bird
import copy


class stage:
    def __init__(self, gravity, max_lv):
        self.screen = Screen()
        self.line = Turtle()
        self.cac = Turtle()
        self.bird = Turtle()
        self.dinosaur = Dinosaur()
        self.text = Texts()
        self.cactus = []
        self.birds = []
        self.gravity = gravity
        self.max_lv = max_lv

    def scree(self):
        self.screen.setup(1000, 700)
        self.screen.bgcolor("light blue")

    def lne(self):
        self.line.hideturtle()
        self.line.penup()
        self.line.setpos(-500, -115)
        self.line.pendown()
        self.line.showturtle()
        self.line.forward(1020)

    def breeze(self):
        self.dinosaur.lil_dino()
        self.dinosaur.height = 200
        self.dinosaur.width = 200

    def jump(self):
        self.dinosaur.update()

    def txt(self):
        self.text.draw_msg()

    def append(self, obs):
        new_obs = copy.deepcopy(obs)
        self.cactus.append(new_obs)

    def append_(self, obs):
        new_obs = copy.deepcopy(obs)
        self.birds.append(new_obs)

    def update(self, dt):
        for cac in self.cactus:
            cac.update(dt)

    def update_(self, dt):
        for bird in self.birds:
            bird.update(dt)

    def render(self):
        self.cac.clear()
        for i in self.cactus:
            i.small_cactus(self.cac)
            self.cac.penup()
            self.cac.speed(2)
            self.cac.goto(-500, i.pos.y)

    def render_(self):
        self.bird.clear()
        for i in self.birds:
            i.birds(self.bird)
            self.bird.penup()
            self.bird.speed(2)
            self.bird.goto(-500, Bird.random_y)
        self.screen.update()


