from modules.linear_algebra.matrix import Matrix
from modules.markov_chains.discrete import DiscreteMarkovChain


class VectorMarkovChain:
    def __init__(self, discrete_chain: DiscreteMarkovChain):
        self.discrete_chain = discrete_chain
        self.matrix = self.discrete_chain.to_matrix()

    def transition(self, state: Matrix) -> Matrix:
        return state.multiply(self.matrix)
