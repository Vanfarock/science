from graphics.components.component import Component, Position, Trail
from graphics.entities.entity import Entity
from graphics.screen import Screen
from graphics.systems.system import System


class TrailSystem(System):
    def __init__(self, screen: Screen):
        self.screen = screen

    def get_required_components(self) -> list[type[Component]]:
        return [Position, Trail]

    def update(self, entities: list[Entity], dt: float) -> None:
        for entity in entities:
            pos = entity.get_component(Position)
            trail = entity.get_component(Trail)
            if pos and trail:
                trail.history.append(pos)
                # trail.history = [Position(x=100, y=100), Position(x=200, y=100)]
                if len(trail.history) > 2:
                    print(trail.history[-1].x, trail.history[-1].y)
                    print(trail.history[-2].x, trail.history[-2].y)
                    print()

                for i in range(len(trail.history) - 1):
                    self.screen.draw_line(
                        trail.history[i].x,
                        trail.history[i].y,
                        trail.history[i + 1].x,
                        trail.history[i + 1].y,
                        trail.color,
                        int(trail.thickness.value),
                    )
