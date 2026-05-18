# Markov Chains

A general Markov Chain library written in Python using a minimal weighted digraph representations and pythonic comprehensions.

## Imports

- math: gcd, prod
- random: choices
- (for visualise.py only) graphiz: Digraph

## Setup

- Setup python environment.
`python -m venv .venv`
- - Shell: `source .venv/bin/activate`
- - Powershell: `.\.venv\bin\activate.ps1`

- Install packages
`pip install -r requirements.txt`

## Usage Examples

### Defining a DTMC

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
