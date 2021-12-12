import pgzero
import pgzrun
from pgzero.actor import Actor
from pgzero.animation import animate

TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8

tiles = ['empty', 'wall', 'goal', 'door', 'key']

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 2, 0, 1],
    [1, 0, 0, 3, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 4, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

player = Actor("walk1.png", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
enemy = Actor("trap1.png", anchor=(0, 0), pos=(3 * TILE_SIZE, 6 * TILE_SIZE))


def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
    player.draw()
    enemy.draw()


def on_key_down(key):
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == key.UP:
        row = row - 1
    if key == key.DOWN:
        row = row + 1
    if key == key.LEFT:
        column = column - 1
    if key == key.RIGHT:
        column = column + 1
    tile = tiles[maze[row][column]]
    if tile == 'empty':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x, y))
    global unlock
    if tile == "goal":
        print("KONIEC GRY, BRAWO!")
        exit()


pgzrun.go()
