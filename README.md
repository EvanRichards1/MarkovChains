# Markov Chains

A general Markov Chain library written in Python using a minimal weighted digraph representations and pythonic comprehensions.

## Imports

- math: gcd, prod
- random: choices
- (for visualise.py only) graphiz: Digraph

## Setup

Setup python environment.
`python -m venv .venv`
- Shell: `source .venv/bin/activate`
- Powershell: `.\.venv\bin\activate.ps1`

Install packages
`pip install -r requirements.txt`

## Usage Examples

```python
from graph import *
import markov_chain as mc
from visualise import visualise

v1: Vertex = Vertex('1')
v2: Vertex = Vertex('2')
v3: Vertex = Vertex('3')
v4: Vertex = Vertex('4')
```

### DTMC 1

```python
dtmc1: Graph = Graph(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 1)
    },
    "dtmc1"
)
```

`> visualise(dtmc1, view=True)`

<img width="1083" height="338" alt="image" src="https://github.com/user-attachments/assets/43ec92a5-c142-435b-ad87-e5f268cf9d32" />

`> mc.run_dtmc(dtmc1, v1, 12)`

`((1), (2), (3), (1), (2), (3), (1), (2), (3), (1), (2), (3), (1))`

### DTMC 2

```python
dtmc2: Graph = Graph(
    {v1, v2, v3, v4},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 0.75),
        Edge(v3, v4, 0.25),
        Edge(v4, v4, 1)
    },
    "dtmc2"
)
```

`> visualise(dtmc2, view=True)`

<img width="1590" height="338" alt="image" src="https://github.com/user-attachments/assets/bc1d74a1-bca6-4680-bff8-c4cc2233f6a7" />

`> mc.summarise(dtmc2)`

```
Sample run: ((1), (2), (3), (1), (2), (3), (1), (2), (3), (1), (2), (3), (1), (2), (3), (1))
Communicating classes: {{(4)}, {(1), (2), (3)}}
Reducible
Periodicities:
- {(4)}: 1
- {(1), (2), (3)}: 3
```

## DTMC 3

```python
dtmc3: Graph = Graph(
    {v1, v2},
    {
        Edge(v1, v2, 1),
        Edge(v2, v1, 1)
    },
    "dtmc3"
)
```

`> visualise(dtmc3, view=True)`

<img width="671" height="203" alt="image" src="https://github.com/user-attachments/assets/779354c3-e96a-4051-a4f0-82f155f3fd7d" />

`> "p_v1,v2^(15) = " + str(mc.trace_n_step_transition_probability(dtmc3, v1, v2, 15))`

`p_v1,v2^(15) = 1`

`> "p_v1,v2^(14) = " + str(mc.trace_n_step_transition_probability(dtmc3, v1, v2, 14))`

`p_v1,v2^(14) = 0`

## Progress

- [x] Weighted digraph representation.
- [x] DTMC sampler.
- [x] n-step transition probability tracing.
- [x] Period tracer.
- [x] State communicating class classifier.
- [x] Is irreducible identifier.
- [x] Is aperiodic identifier.
- [x] Tests for past features.
- [x] DTMC summariser.
- [x] Quick DTMC visualiser using graphviz.Digraph.
- [ ] Add tests for upcoming features.
- [ ] Deductive hitting probability/time tracer.
- [ ] Recurrence/transience classifier.
- [ ] Positive/null recurrent classifier.
- [ ] Stationary distribution finder.
- [ ] Deductive convergence identifier.
- [ ] Reversibility/queue identifier.
- [ ] CTMC variation + sampler.
- [ ] Explosivity identifier.
