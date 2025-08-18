from graphics.components.component import Component, Position, Velocity
from graphics.entities.entity import Entity
from graphics.systems.system import System


class MovementSystem(System):
    def get_required_components(self) -> list[type[Component]]:
        return [Position, Velocity]

    def update(self, entities: list[Entity], dt: float) -> None:
        for entity in entities:
            pos = entity.get_component(Position)
            vel = entity.get_component(Velocity)
            if pos and vel:
                pos.x += vel.dx * dt
                pos.y += vel.dy * dt
