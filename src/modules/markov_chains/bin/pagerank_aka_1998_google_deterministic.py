from modules.linear_algebra.matrix import Matrix
from modules.markov_chains.chain import MarkovState
from modules.markov_chains.discrete import DiscreteMarkovChain
from modules.markov_chains.vector import VectorMarkovChain


def main():
    iterations = 1_000_000
    damping_factor = 0.85
    chain = build_chain()
    N = chain.matrix.rows
    state = Matrix(1, N, default_value=1.0) / N
    teleport = Matrix(1, N, default_value=1.0) / N
    tolerance = 1e-6

    for _ in range(100):
        new_state = (
            damping_factor * state.multiply(chain.matrix)
            + (1 - damping_factor) * teleport
        )
        if (new_state - state).normalize(1) < tolerance:
            break
        state = new_state
    print(state)


def build_chain() -> VectorMarkovChain:
    chain = DiscreteMarkovChain()
    a = MarkovState("A")
    b = MarkovState("B")
    c = MarkovState("C")
    d = MarkovState("D")
    e = MarkovState("E")
    chain.add_transition(a, b, 0.5)
    chain.add_transition(a, c, 0.5)
    chain.add_transition(b, c, 1.0)
    chain.add_transition(c, a, 1.0)
    chain.add_transition(d, c, 1.0)
    chain.add_transition(e, c, 0.5)
    chain.add_transition(e, d, 0.5)
    chain.build()
    return VectorMarkovChain(chain)


if __name__ == "__main__":
    main()
