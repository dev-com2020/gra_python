import random

import pgzrun

from pgzero.keyboard import keyboard

from pgzhelper import *

WIDTH = 800
HEIGHT = 600
# BACKG = "back.png"
background_image = "back.png"
backgrounds = []
BACKG = Actor(background_image)
backgrounds.append(BACKG)
BACKG.scale = 0.9
BACKG.x = 100
BACKG.y = 60
BACKG = Actor(background_image)
BACKG.scale = 0.9
BACKG.x = -100
BACKG.y = 60
backgrounds.append(BACKG)

runner = Actor('walk1.png')
run_images = ['walk1.png', 'walk2.png', 'walk3.png']
runner.images = run_images
runner.x = 100
runner.y = 300
runner.scale = 2
runner.fps = 8

velocity_y = 0
gravity = 1

obstacles = []
obstacles_timeout = 0

score = 0
game_over = False


def update():
    # runner.next_image()  # wyświetla kolejne obrazy postaci
    runner.animate()
    global velocity_y, obstacles_timeout, score, game_over

    if not game_over:

        obstacles_timeout += 1
        if obstacles_timeout > 50:
            actor = Actor('rock2.png')
            actor.x = 850
            actor.y = 400
            actor.scale = 2
            obstacles.append(actor)
            obstacles_timeout = 0

        for actor in obstacles:
            actor.x -= 8
            if actor.x < -10:
                obstacles.remove(actor)
                score += 1

        if runner.y == 400:
            if keyboard.up:
                velocity_y = -15

        runner.y += velocity_y
        velocity_y += gravity
        if runner.y > 400:
            velocity_y = 0
            runner.y = 400

        if runner.collidelist(obstacles) != -1:
            game_over = True

        for BACKG in backgrounds:
            BACKG.x -= 2
            if BACKG.x > 800:
                BACKG.x = - 600
            BACKG.image = background_image


def draw():
    # screen.draw.filled_rect(Rect(0, 0, 800, 400), (163, 232, 254))
    # screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))

    for BACKG in backgrounds:
        BACKG.draw()

    if game_over:
        screen.draw.text('KONIEC GRY !!!', centerx=400, centery=200, color=(255, 255, 255), fontsize=60)
        screen.draw.text('WYNIK:' + str(score), centerx=400, centery=300, color=(255, 255, 255), fontsize=60)

    else:
        runner.draw()
        for actor in obstacles:
            actor.draw()
        screen.draw.text('WYNIK:' + str(score), (15, 10), color=(255, 255, 255), fontsize=30)


pgzrun.go()
