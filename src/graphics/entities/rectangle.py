from graphics.components.component import Color, Position, Size
from graphics.entities.entity import Entity


class Rectangle(Entity):
    def __init__(
        self, position: Position, size: Size, color: Color, id: str | None = None
    ):
        super().__init__(id)
        self.add_component(position)
        self.add_component(size)
        self.add_component(color)
