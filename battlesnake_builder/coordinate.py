from __future__ import annotations
import math


class Coordinate():
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) is Coordinate:
            return Coordinate(self.x + other.x, self.y + other.y)
        else:
            raise ValueError()

    def real_distance(self, other: Coordinate):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def manhattan_distance(self, other: Coordinate):
        return (self.x - other.x) + (self.y - other.y)
