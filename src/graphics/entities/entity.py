import uuid
from typing import TypeVar, cast

from graphics.components.component import Component

T = TypeVar("T", bound=Component)


class Entity:
    def __init__(self, id: str | None = None):
        self.id = id or str(uuid.uuid4())
        self.components: dict[type[Component], Component] = {}

    def add_component(self, component: Component) -> None:
        self.components[type(component)] = component

    def get_component(self, component_type: type[T]) -> T | None:
        component = self.components.get(component_type)
        return cast(T, component) if component is not None else None
