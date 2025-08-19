from graphics.common.anchor import get_anchored_position
from graphics.components.component import Anchor, Component, Position, Size, Trail
from graphics.entities.entity import Entity
from graphics.screen import Screen
from graphics.systems.system import System


class TrailSystem(System):
    def __init__(self, screen: Screen):
        self.screen = screen

    def get_required_components(self) -> list[type[Component]]:
        return [Position, Size, Trail, Anchor]

    def update(self, entities: list[Entity], dt: float) -> None:
        for entity in entities:
            pos = entity.get_component(Position)
            size = entity.get_component(Size)
            trail = entity.get_component(Trail)
            anchor = entity.get_component(Anchor)
            if pos and size and trail and anchor:
                trail.history.append(get_anchored_position(pos, size, anchor.anchor))
                if trail.max_length and len(trail.history) > trail.max_length:
                    trail.history.pop(0)

                # for i in range(len(trail.history) - 1):
                #     self.screen.draw_line(
                #         trail.history[i].x,
                #         trail.history[i].y,
                #         trail.history[i + 1].x,
                #         trail.history[i + 1].y,
                #         trail.color,
                #         int(trail.thickness.value),
                #     )
