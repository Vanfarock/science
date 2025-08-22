import random
import unicodedata

from modules.linear_algebra.matrix import Matrix
from modules.markov_chains.chain import MarkovState
from modules.markov_chains.discrete import DiscreteMarkovChain
from modules.markov_chains.vector import VectorMarkovChain


def main():
    book_content = load_book_content("crime_and_punishment")
    book_tokens = tokenize_book(book_content)
    analysis = analyze_1st_order_tokens(book_tokens)

    i = 0
    for token, next_token in analysis.items():
        print(token, next_token)
        i += 1
        if i > 100:
            break

    chain = build_chain(analysis)
    state = Matrix(1, chain.matrix.rows, default_value=1.0 / chain.matrix.rows)
    tokens = list(analysis.keys())

    for _ in range(100):
        word = random.choices(tokens, weights=state.data[0], k=1)[0]
        print(word)
        state = state.multiply(chain.matrix)


def load_book_content(book_name: str) -> str:
    with open(f"assets/books/{book_name}.txt", "r", encoding="utf-8") as file:
        return file.read()


def tokenize_book(book_content: str) -> list[str]:
    book_content = book_content.lower()
    cleaned_content = "".join(
        ch for ch in book_content if not unicodedata.category(ch).startswith("P")
    )

    return cleaned_content.split()


def analyze_1st_order_tokens(tokens: list[str]) -> dict[str, dict[str, int]]:
    analysis = {}
    for i in range(len(tokens)):
        token = tokens[i]
        if i == len(tokens) - 1:
            analysis[token] = {tokens[0]: 1.0}
            continue
        next_token = tokens[i + 1]
        if token in analysis:
            if next_token in analysis[token]:
                analysis[token][next_token] += 1
            else:
                analysis[token][next_token] = 1
        else:
            analysis[token] = {next_token: 1}
    return analysis


def build_chain(token_analysis: dict[str, dict[str, int]]) -> VectorMarkovChain:
    discrete_chain = DiscreteMarkovChain()
    for token, next_tokens in token_analysis.items():
        total_count = sum(next_tokens.values())
        token_state = MarkovState(token)
        for next_token, count in next_tokens.items():
            next_token_state = MarkovState(next_token)
            discrete_chain.add_transition(
                token_state,
                next_token_state,
                count / total_count,
            )
        total_probability = discrete_chain.validate_state(token_state)
        if total_probability != 1.0:
            discrete_chain.nodes[token_state][0].probability += 1 - total_probability
    discrete_chain.build()

    chain = VectorMarkovChain(discrete_chain)
    return chain


if __name__ == "__main__":
    main()
