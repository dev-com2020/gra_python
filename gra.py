import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.rect import Rect
from pgzhelper import *

WIDTH = 800
HEIGHT = 600
#BACKG = "back.png"
BACKG = Actor("back.png")
BACKG.scale = 0.9
BACKG.x = 100
BACKG.y = 60


runner = Actor('walk.png')
run_images = ['walk.png']
runner.images = run_images
runner.x = 100
runner.y = 400
runner.scale = 2
runner.fps = 10

velocity_y = 0
gravity = 1

obstacles = []
obstacles_timeout = 0


def update():
    runner.next_image()  # wyświetla kolejne obrazy postaci
    runner.animate()
    global velocity_y, obstacles_timeout

    obstacles_timeout += 1
    if obstacles_timeout > 50:
        actor = Actor('rock2.png')
        actor.x = 850
        actor.y = 430
        actor.scale = 2
        obstacles.append(actor)
        obstacles_timeout = 0

    for actor in obstacles:
        actor.x -= 8

    if keyboard.up:
        velocity_y = -15

    runner.y += velocity_y
    velocity_y += gravity
    if runner.y > 400:
        velocity_y = 0
        runner.y = 400


def draw():
    # screen.draw.filled_rect(Rect(0, 0, 800, 400), (163, 232, 254))
    # screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))
    BACKG.draw()
    runner.draw()
    for actor in obstacles:
        actor.draw()


pgzrun.go()
