# Science

A couple of applied science knowledge

## Contents

* [Markov Chains](#markov-chains)

### Markov Chains

**2D Random Walk**

Simple 2D Random Walk using Markov Chains with a probability of 25% of going to each direction

![2D Random Walk](assets/gifs/random_walk_2d.gif)

**Simple Weather Prediction**

This weather prediction simulates a person in a dark room, without any windows and without knowing the weather outside that day. The input for the Markov chain is therefore a probability vector of whether the weather is Sunny, Cloudy, or Rainy. After each day, the person discovers what the previous day’s weather was, and based on these transitions, the probability state eventually converges to specific probabilities for each type of weather.

The simulation below shows the evolution of the state vector. At first, the person thought there was a 70% chance of it being sunny, but as the days passed, they noticed there was a much higher chance of it being rainy. Pretty depressing for someone locked in a room!

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
