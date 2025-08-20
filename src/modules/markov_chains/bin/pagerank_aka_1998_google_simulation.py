import random

from modules.markov_chains.chain import MarkovState
from modules.markov_chains.discrete import DiscreteMarkovChain


def main():
    iterations = 1_000_000
    damping_factor = 0.85
    chain = build_chain()
    state = chain.get_random_discrete_state()

    relevance = {}
    for _ in range(iterations):
        relevance[state] = relevance.get(state, 0) + 1
        if random.random() > damping_factor:
            state = chain.get_random_discrete_state()
            continue

        transition = chain.get_random_transition(state)
        if transition is None:
            break
        state = transition.to_state

    rank = sorted(relevance.items(), key=lambda x: x[1], reverse=True)
    total_score = sum(score for _, score in rank)
    for state, score in rank:
        print(f"{state}: {score / total_score}")


def build_chain() -> DiscreteMarkovChain:
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
    return chain


if __name__ == "__main__":
    main()
