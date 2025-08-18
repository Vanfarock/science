from graphics.components.component import Color, Component, Position, Size
from graphics.entities.entity import Entity
from graphics.screen import Screen
from graphics.systems.system import System


class RenderSystem(System):
    def __init__(self, screen: Screen):
        self.screen = screen

    def get_required_components(self) -> list[type[Component]]:
        return [Position, Size, Color]

    def update(self, entities: list[Entity], dt: float) -> None:
        for entity in entities:
            pos = entity.get_component(Position)
            size = entity.get_component(Size)
            color = entity.get_component(Color)
            if pos and size and color:
                self.screen.draw_rectangle(pos.x, pos.y, size.width, size.height, color)
