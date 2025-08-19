from modules.linear_algebra.matrix import Matrix
from modules.markov_chains.chain import MarkovChain, MarkovState


def main():
    chain = build_chain()
    state = chain.get_first_random_state()

    m = Matrix(3, 2, [[1.0, 2.22], [3.0, 4.0], [5.0, 6.0]])
    print(m)

    print()
    print(m.transpose())


def build_chain() -> MarkovChain:
    chain = MarkovChain()
    sunny = MarkovState("Sunny")
    cloudy = MarkovState("Cloudy")
    rainy = MarkovState("Rainy")
    chain.add_transition(sunny, sunny, 0.7)
    chain.add_transition(sunny, cloudy, 0.1)
    chain.add_transition(sunny, rainy, 0.2)
    chain.add_transition(cloudy, sunny, 0.2)
    chain.add_transition(cloudy, cloudy, 0.3)
    chain.add_transition(cloudy, rainy, 0.5)
    chain.add_transition(rainy, sunny, 0.1)
    chain.add_transition(rainy, cloudy, 0.3)
    chain.add_transition(rainy, rainy, 0.6)
    chain.build()
    return chain


if __name__ == "__main__":
    main()
