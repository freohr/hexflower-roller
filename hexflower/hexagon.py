
from hexflower.direction import Direction


class Hexagon:
    id = 0
    content = ""
    neighbours = {
        Direction.self: 0,
        Direction.top: 1,
        Direction.top_right: 2,
        Direction.bottom_right: 3,
        Direction.bottom_left: 4,
        Direction.bottom: 5,
        Direction.top_left: 6,
    }

    def __init__(self, id: int, content: str, neighbours: dict) -> None:
        self.id = id
        self.content = content
        self.neighbours = neighbours
        pass

    def __repr__(self):
        return f"Hexagon(id='{self.id}', content='{self.content}', neighbours='{self.neighbours}')"
        pass

    def __str__(self):
        return f"Hex {self.id}, containing \"{self.content}\""

    def get_neighbour(self, direction: Direction):
        neighbour = self.neighbours.get(direction)
        return neighbour if neighbour is not None else self.id
