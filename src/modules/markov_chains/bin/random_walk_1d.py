from graphics.components.component import (
    Color,
    Position,
    Size,
    Thickness,
    Trail,
    Velocity,
)
from graphics.entities.rectangle import Rectangle
from graphics.view import View
from graphics.world import World
from modules.markov_chains.chain import MarkovChain, MarkovState


def main():
    world = World()

    square = Rectangle(
        Position(x=600, y=300),
        Size(width=10, height=10),
        Color.black(),
    )
    square.add_component(Velocity(dx=10, dy=0))
    square.add_component(
        Trail(
            color=Color.red(),
            thickness=Thickness(value=5),
            history=[],
        )
    )
    world.add_entity(square)

    view = View(world, width=1280, height=720)
    view.show()

    chain = build_chain()


def build_chain() -> MarkovChain:
    chain = MarkovChain()
    left_state = MarkovState("Go Left")
    right_state = MarkovState("Go Right")
    chain.add_transition(left_state, right_state, 0.5)
    chain.add_transition(left_state, left_state, 0.5)
    chain.add_transition(right_state, left_state, 0.5)
    chain.add_transition(right_state, right_state, 0.5)
    chain.build()
    return chain


if __name__ == "__main__":
    main()
