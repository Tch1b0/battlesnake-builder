from battlesnake_builder.coordinate import Coordinate
from battlesnake_builder.snake import Snake


class Board():
    height: int
    width: int
    food: list[Coordinate]
    hazards: list[Coordinate]
    snakes: list[Snake]

    def closest_food(self, snake: Snake) -> Coordinate:
        return sorted(self.food, key=lambda x: snake.head.coord.manhattan_distance(x))[0]

    def closest_snake(self, snake: Snake) -> Snake | None:
        if len(self.snakes) <= 1:
            return None

        lowest_dist = -1
        lowest_dist_snake = None

        for other_snake in self.snakes:
            if other_snake == snake:
                continue
            for body_part in (other_snake.body + other_snake.head):
                distance = body_part.coord.manhattan_distance(snake.head.coord)
                if distance < lowest_dist or lowest_dist == -1:
                    lowest_dist = distance
                    lowest_dist_snake = other_snake
                    break

        return lowest_dist_snake

    @classmethod
    def from_json(cls, json: dict):
        board = cls()
        board.height = json["height"]
        board.width = json["width"]
        board.food = [Coordinate(x["x"], x["y"]) for x in json["food"]]
        board.hazards = [Coordinate(x["x"], x["y"]) for x in json["hazards"]]
        board.snakes = [Snake.from_json(x) for x in json["snakes"]]
        return board
