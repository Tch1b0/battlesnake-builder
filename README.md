# battlesnake-builder

Easily build a battlesnake in python

## installation

```
$ pip install battlesnake_builder
```

## Examples

### Basic snake that always moves up

```py
from battlesnake_builder import BattleSnake, Config

my_snake = BattleSnake()

@my_snake.on_turn
def turn(data):
    return "up"

my_snake.run()
```

### More advanced snake that looks for food

```py
from battlesnake_builder import BattleSnake, Config

my_snake = BattleSnake()

@my_snake.on_turn
def turn(data):
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
```

### Snake with static config

```py
my_snake = BattleSnake(Config(apiversion="0.1"))
```

Or

```py
my_snake = BattleSnake({
    "apiversion": "0.1"
})
```

### Snake with dynamic config

```py
from battlesnake_builder import BattleSnake
import random

my_snake = BattleSnake()

@my_snake.on_config
def config():
    tails = ["default","curled"]
    return {
        "tail": random.choice(tails)
    }

my_snake.run()
```

You can also mix a static and dynamic config. If you overwrite an existing value, the newer one is getting adapted.
