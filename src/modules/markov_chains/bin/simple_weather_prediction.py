from modules.linear_algebra.matrix import Matrix
from modules.markov_chains.chain import MarkovState
from modules.markov_chains.discrete import DiscreteMarkovChain
from modules.markov_chains.vector import VectorMarkovChain


def main():
    chain = build_chain()
    state = Matrix(1, 3, [[0.7, 0.2, 0.1]])

    for day in range(10):
        print(state)
        state = chain.transition(state)
    print(state)


def build_chain() -> VectorMarkovChain:
    discrete_chain = DiscreteMarkovChain()
    sunny = MarkovState("Sunny")
    cloudy = MarkovState("Cloudy")
    rainy = MarkovState("Rainy")
    discrete_chain.add_transition(sunny, sunny, 0.7)
    discrete_chain.add_transition(sunny, cloudy, 0.1)
    discrete_chain.add_transition(sunny, rainy, 0.2)
    discrete_chain.add_transition(cloudy, sunny, 0.2)
    discrete_chain.add_transition(cloudy, cloudy, 0.3)
    discrete_chain.add_transition(cloudy, rainy, 0.5)
    discrete_chain.add_transition(rainy, sunny, 0.1)
    discrete_chain.add_transition(rainy, cloudy, 0.3)
    discrete_chain.add_transition(rainy, rainy, 0.6)
    discrete_chain.build()

    chain = VectorMarkovChain(discrete_chain)
    return chain


if __name__ == "__main__":
    main()
