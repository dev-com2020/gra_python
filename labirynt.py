from pgzero.actor import Actor

TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8

tiles = ['empty', 'wall', 'goal']

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

player = Actor("alien", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))


