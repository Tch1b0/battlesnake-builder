# battlesnake-builder

Easily build a battlesnake in python

## Installation

```bash
$ pip install battlesnake_builder
```

## Requirements

-   python >= 3.10
-   Flask >= 2.0.2

## Examples

### Basic snake that always moves up

```py
from battlesnake_builder import BattleSnake

my_snake = BattleSnake()

@my_snake.on_move
def move(data, _store):
    return "up"

my_snake.run()
```

### More advanced snake that looks for food

```py
from battlesnake_builder import BattleSnake

my_snake = BattleSnake()


@my_snake.on_move
def move(data, _store):
    me = data.you
    closest_food = data.board.closest_food(me)

    return me.head.coord.direction_to(closest_food)


my_snake.run()

```

### Snake with static config

```py
from battlesnake_builder import BattleSnake, Config

my_snake = BattleSnake(Config(apiversion="0.1"))
```

Or

```py
from battlesnake_builder import BattleSnake

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

### Shout something

```py
@my_snake.on_move
def move(_data, _store):
    return {
        "move": "up",
        "shout": "WHY ARE WE SHOUTING"
    }
```

### Snake that stores data across events

```py
from battlesnake_builder import BattleSnake

my_snake = BattleSnake()

@my_snake.on_start
def start(data, store):
    store["snake_amount"] = len(data.board.snakes)

@my_snake.on_move
def end(data, store):
    shout = "Everyone is alive"
    if len(data.board.snakes) < store["snake_amount"]:
        shout = "Some snake died!"

    return {
        "move": "up",
        "shout": shout
    }

my_snake.run()
```

### All features

```py
from battlesnake_builder import BattleSnake, Config, Data

my_snake = BattleSnake(Config(tail="curly"))

@my_snake.on_config
def config():
    return {
        "head": "default"
    }

@my_snake.on_start
def start(data: Data, store: dict):
    store["start_snake_size"] = len(data.board.snakes)

@my_snake.on_move
def move(data: Data, store: dict):
    shout = "Everything is fine"
    if store["start_snake_size"] != len(data.board.snakes):
        shout = "Oh no! Someone lost :("

    for m in ["up", "down", "left", "right"]:
        if data.board.is_move_safe(data.you, m):
            return {
                "move": m,
                "shout": shout
            }
    return {
        "move": "up",
        "shout": shout
    }

@my_snake.on_end
def end(data: Data, store: dict):
    end_snake_size = len(data.board.snakes)
    print(f"Out of {store['start_snake_size']} Snakes, only {end_snake_size} survived")


my_snake.run()
```
