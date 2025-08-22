from random import choice, random

from modules.linear_algebra.matrix import Matrix
from modules.markov_chains.chain import MarkovState, MarkovTransition
from modules.markov_chains.errors import InvalidMarkovChainError


class DiscreteMarkovChain:
    def __init__(self):
        self.nodes: dict[MarkovState, list[MarkovTransition]] = {}
        self.finished = False

    def add_transition(
        self, from_state: MarkovState, to_state: MarkovState, probability: float
    ):
        transition = MarkovTransition(from_state, to_state, probability)

        state = self.nodes.get(from_state)
        if state is None:
            self.nodes[from_state] = [transition]
        else:
            self.nodes[from_state].append(transition)

    def validate(self) -> None:
        for state, transitions in self.nodes.items():
            total_probability = self.validate_state(state)
            if total_probability != 1.0:
                raise InvalidMarkovChainError(
                    state=state.name, probability=total_probability
                )

    def validate_state(self, state: MarkovState) -> float:
        transitions = self.nodes.get(state)
        if transitions is None:
            return 0.0
        return sum(t.probability for t in transitions)

    def build(self, raise_error: bool = True) -> None:
        try:
            self.validate()
        except InvalidMarkovChainError as e:
            if raise_error:
                raise e
            else:
                print(f"WARNING: {e.message}")

        self.finished = True

    def get_random_discrete_state(self) -> MarkovState:
        return choice(list(self.nodes.keys()))

    def get_random_transition(self, state: MarkovState) -> MarkovTransition | None:
        probability = random()

        total_probability = 0.0
        for transition in self.nodes[state]:
            if probability < total_probability + transition.probability:
                return transition
            total_probability += transition.probability

        return None

    def to_matrix(self) -> Matrix:
        matrix = Matrix(
            rows=len(self.nodes.keys()), cols=len(self.nodes.keys()), default_value=0.0
        )
        for i, (state, transitions) in enumerate(self.nodes.items()):
            for transition in transitions:
                j = list(self.nodes.keys()).index(transition.to_state)
                matrix.set(i, j, transition.probability)
        return matrix
