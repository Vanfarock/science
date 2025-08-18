from graphics.components.component import Component
from graphics.entities.entity import Entity


class System:
    def get_required_components(self) -> list[type[Component]]:
        raise NotImplementedError

    def update(self, entities: list[Entity], dt: float) -> None:
        raise NotImplementedError
