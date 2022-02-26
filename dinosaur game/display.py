from turtle import Screen
from stage import stage
from obstacles import Obstacles
from bird import Bird
from vector import Vector
from random import randint


scr = Screen()
scr.title('DINOFLY GAME')
stage = stage(-0.5, 700)
stage.scree()
stage.lne()
stage.txt()
dino = stage.breeze()
ground_lv = -50
score = 0
speed = 50


scr.onkeypress(stage.jump, 'space')
scr.listen()

obs = 1
for i in range(obs):
    random = randint(500, 1200)
    small_cac = Obstacles(Vector(random, ground_lv))
    stage.append(small_cac)

for i in range(obs):
    random = randint(500, 1200)
    small_bird = Bird(Vector(random, Bird.random_y))
    stage.append_(small_bird)

while True:
    stage.update(speed)
    stage.update_(speed)
    stage.render()
    stage.render_()
    stage.gra()
    scr.update()
