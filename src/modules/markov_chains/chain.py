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
