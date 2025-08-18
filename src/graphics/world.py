from collections import defaultdict

from graphics.components.component import Component
from graphics.entities.entity import Entity
from graphics.systems.system import System


class World:
    def __init__(self):
        self.entities: set[Entity] = set()
        self.components_map: dict[type[Component], set[Entity]] = defaultdict(set)

        self.systems: list[System] = []

    def add_entity(self, entity: Entity):
        self.entities.add(entity)

        for component in entity.components:
            self.components_map[component].add(entity)

    def get_entities_with(self, *component_types) -> set[Entity]:
        return {
            entity
            for entity in self.entities
            if all(component in entity.components for component in component_types)
        }

    def update(self, dt: float):
        for system in self.systems:
            entities = self.get_entities_with(*system.get_required_components())
            system.update(list(entities), dt)
