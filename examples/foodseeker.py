from battlesnake_builder import BattleSnake

my_snake = BattleSnake()


@my_snake.on_move
def move(data, _store):
    me = data.you
    closest_food = data.board.closest_food(me)

    if closest_food.y > me.head.coord.y:
        return "up"
    elif closest_food.y < me.head.coord.y:
        return "down"

    if closest_food.x > me.head.coord.x:
        return "right"

    return "left"


my_snake.run()
