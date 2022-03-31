"""
A snake that always moves up
"""

from battlesnake_builder import BattleSnake

snake = BattleSnake()


@snake.on_move
def move(_data, _store):
    return "up"


snake.run()
