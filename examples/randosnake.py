"""
This snake only makes random moves and always has a new look
"""

from battlesnake_builder import BattleSnake
import random

snake = BattleSnake()


@snake.on_config
def config():
    tails = ["block-bum", "curled", "pixel", "skinny", "small-rattle"]
    heads = ["beluga", "bendr", "dead", "evil", "fang", "shades", "smile"]
    return {
        "head": random.choice(heads),
        "tail": random.choice(tails)
    }


@snake.on_move
def move(_data):
    choices = ["up", "down", "left", "right"]
    return random.choice(choices)


snake.run()
