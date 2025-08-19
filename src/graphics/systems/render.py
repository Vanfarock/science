from graphics.components.component import Color, Component, Position, Size, Trail
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
            trail = entity.get_component(Trail)
            if trail:
                for i in range(len(trail.history) - 1):
                    self.screen.draw_line(
                        trail.history[i].x,
                        trail.history[i].y,
                        trail.history[i + 1].x,
                        trail.history[i + 1].y,
                        trail.color.gradient(Color.white(), i / len(trail.history)),
                        int(trail.thickness.value),
                    )

            pos = entity.get_component(Position)
            size = entity.get_component(Size)
            color = entity.get_component(Color)
            if pos and size and color:
                self.screen.draw_rectangle(pos.x, pos.y, size.width, size.height, color)
