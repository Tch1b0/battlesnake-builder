from battlesnake_builder import BattleSnake

my_snake = BattleSnake()


@my_snake.on_move
def move(data):
    me = data.you
    closest_food = data.board.closest_food(me)

    if closest_food.coord.y > me.coord.y:
        return "up"
    elif closest_food.coord.y < me.coord.y:
        return "down"

    if closest_food.coord.x > me.coord.x:
        return "right"

    return "left"


my_snake.run()
