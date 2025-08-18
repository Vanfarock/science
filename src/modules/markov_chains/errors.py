class InvalidMarkovChainError(Exception):
    def __init__(self, state: str, probability: float):
        self.message = (
            f"Invalid state '{state}' with total probability of {probability}"
        )
        super().__init__(self.message)
