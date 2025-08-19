from dataclasses import dataclass

from graphics.common.enums import AnchorTypeEnum
from graphics.components.component import (
    Anchor,
    Color,
    Component,
    Position,
    Size,
    Thickness,
    Trail,
    Velocity,
)
from graphics.entities.entity import Entity
from graphics.entities.rectangle import Rectangle
from graphics.systems.system import System
from graphics.view import View
from graphics.world import World
from modules.markov_chains.chain import MarkovChain, MarkovState


@dataclass
class RandomWalkComponent(Component):
    state: MarkovState


class RandomWalk2DSystem(System):
    def __init__(self, chain: MarkovChain):
        self.chain = chain

    def get_required_components(self) -> list[type[Component]]:
        return [Velocity, RandomWalkComponent]

    def update(self, entities: list[Entity], dt: float) -> None:
        for entity in entities:
            velocity = entity.get_component(Velocity)
            random_walk = entity.get_component(RandomWalkComponent)
            if velocity and random_walk:
                transition = self.chain.get_random_transition(random_walk.state)
                print(transition)
                if transition is None:
                    velocity.dx = 0
                elif transition.to_state.name == "Go Left":
                    velocity.dx = -abs(velocity.dx)
                elif transition.to_state.name == "Go Right":
                    velocity.dx = abs(velocity.dx)
                elif transition.to_state.name == "Go Up":
                    velocity.dy = -abs(velocity.dy)
                elif transition.to_state.name == "Go Down":
                    velocity.dy = abs(velocity.dy)


def main():
    chain = build_chain()
    state = chain.get_first_random_state()

    world = World()
    square = Rectangle(
        Position(x=600, y=300),
        Size(width=10, height=10),
        Color.navy(),
    )
    square.add_component(Velocity(dx=200, dy=200))
    square.add_component(
        Trail(
            color=Color.light_purple(),
            thickness=Thickness(value=8),
            history=[],
            max_length=1000,
        )
    )
    square.add_component(Anchor(anchor=AnchorTypeEnum.CENTER))
    square.add_component(RandomWalkComponent(state=state))
    world.add_entity(square)

    view = View(world, width=1280, height=720)
    view.add_system(RandomWalk2DSystem(chain))
    view.show()


def build_chain() -> MarkovChain:
    chain = MarkovChain()
    left_state = MarkovState("Go Left")
    right_state = MarkovState("Go Right")
    up_state = MarkovState("Go Up")
    down_state = MarkovState("Go Down")
    chain.add_transition(left_state, right_state, 0.25)
    chain.add_transition(left_state, left_state, 0.25)
    chain.add_transition(left_state, up_state, 0.25)
    chain.add_transition(left_state, down_state, 0.25)
    chain.add_transition(right_state, left_state, 0.25)
    chain.add_transition(right_state, right_state, 0.25)
    chain.add_transition(right_state, up_state, 0.25)
    chain.add_transition(right_state, down_state, 0.25)
    chain.add_transition(up_state, up_state, 0.25)
    chain.add_transition(up_state, down_state, 0.25)
    chain.add_transition(up_state, left_state, 0.25)
    chain.add_transition(up_state, right_state, 0.25)
    chain.add_transition(down_state, up_state, 0.25)
    chain.add_transition(down_state, down_state, 0.25)
    chain.add_transition(down_state, left_state, 0.25)
    chain.add_transition(down_state, right_state, 0.25)
    chain.build()
    return chain


if __name__ == "__main__":
    main()
