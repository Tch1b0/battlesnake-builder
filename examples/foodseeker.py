"""
A snake that moves to the closest food
"""

from battlesnake_builder import BattleSnake

my_snake = BattleSnake()


@my_snake.on_move
def move(data, _store):
    me = data.you
    closest_food = data.board.closest_food(me)

    return me.head.coord.direction_to(closest_food)


my_snake.run()
