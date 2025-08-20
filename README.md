# Science

A couple of applied science knowledge

## Contents

- [Markov Chains](#markov-chains)

### Markov Chains

**2D Random Walk**

Simple 2D Random Walk using Markov Chains with a probability of 25% of going to each direction

![2D Random Walk](assets/gifs/random_walk_2d.gif)

**Simple Weather Prediction**

This weather prediction simulates a person in a dark room, without any windows and without knowing the weather outside that day. The input for the Markov chain is therefore a probability vector of whether the weather is Sunny, Cloudy, or Rainy. After each day, the person discovers what the previous day’s weather was, and based on these transitions, the probability state eventually converges to specific probabilities for each type of weather.

The simulation below shows the evolution of the state vector. At first, the person thought there was a 70% chance of it being sunny, but as the days passed, they noticed there was a much higher chance of it being rainy. Kinda depressing for someone locked in a room!

```
         Sunny           Cloudy          Rainy
t = 0  | 0.7           | 0.2           | 0.1           |
t = 1  | 0.54          | 0.16          | 0.3           |
t = 2  | 0.44          | 0.192         | 0.368         |
t = 3  | 0.3832        | 0.212         | 0.4048        |
t = 4  | 0.35112       | 0.22336       | 0.42552       |
t = 5  | 0.333008      | 0.229776      | 0.437216      |
t = 6  | 0.3227824     | 0.2333984     | 0.4438192     |
t = 7  | 0.31700928    | 0.23544352    | 0.4475472     |
t = 8  | 0.31374992    | 0.236598144   | 0.449651936   |
t = 9  | 0.3119097664  | 0.237250016   | 0.4508402176  |
t = 10 | 0.31087086144 | 0.23761804672 | 0.45151109184 |
```

**Google 1998's PageRank**

The idea of this algorithm is ranking websites based on their "influence" across the entire net. The markov chain is structured in a way that the websites with most hyperlinks referencing it, will have greater relevance over others. There is also a damping factor to prevent from dead ends (if the website I'm currently in has no outgoing links). The intuition behind the damping factor is as if the user randomly access any website (teleportation).

There are two ways to do the Page Rank:

- Simulation: simulates that a user is surfing the web using the Markov Chain principles. In the end we will have a count of how many visits each website had and therefore rank them accordingly.

- Deterministic: apply some matrix operations to a Vector State, giving a "damping_factor" importance to websites accessed via hyperlinks and "1 - damping_factor" importance to random websites access (teleportation). The result is a Vector State with the probabilities of each website being accessed in that moment. Higher probabilities equals higher relevance

Given a simple web structure like (each letter is a website):

- A -> B or C
- B -> C
- C -> A
- D -> C
- E -> C or D

The results of both Simulation and Deterministic approach can be seen below:

Simulation

```
C: 0.386606
A: 0.358539
B: 0.182162
D: 0.042803
E: 0.029890
```

Deterministic

```
C: 0.386433
A: 0.358468
B: 0.182349
D: 0.042750
E: 0.030000
```
