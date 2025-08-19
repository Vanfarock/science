from random import choice, random

from modules.markov_chains.errors import InvalidMarkovChainError


class MarkovState:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class MarkovTransition:
    def __init__(
        self, from_state: MarkovState, to_state: MarkovState, probability: float
    ):
        self.from_state = from_state
        self.to_state = to_state
        self.probability = probability

    def __str__(self) -> str:
        return f"{self.from_state} -> {self.to_state} ({self.probability})"


class MarkovChain:
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
            total_probability = sum(t.probability for t in transitions)
            if total_probability != 1.0:
                raise InvalidMarkovChainError(
                    state=state.name, probability=total_probability
                )

    def build(self, raise_error: bool = True) -> None:
        try:
            self.validate()
        except InvalidMarkovChainError as e:
            if raise_error:
                raise e
            else:
                print(f"WARNING: {e.message}")

        self.finished = True

    def get_first_random_state(self) -> MarkovState:
        return choice(list(self.nodes.keys()))

    def get_random_transition(self, state: MarkovState) -> MarkovTransition | None:
        probability = random()

        total_probability = 0.0
        for transition in self.nodes[state]:
            if probability < total_probability + transition.probability:
                return transition
            total_probability += transition.probability

        return None
