from battlesnake_builder import BattleSnake

snake = BattleSnake({
    "apiversion": "42"
})

print(snake.config.to_json())
