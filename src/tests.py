from graph import *
import markov_chain as mc
from math import isclose

v1 = Vertex('1')
v2 = Vertex('2')
v3 = Vertex('3')
v4 = Vertex('4')

dtmc1: mc.DTMC = mc.DTMC(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 1)
    }
)

dtmc2: mc.DTMC = mc.DTMC(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v2, 2/3),
        Edge(v2, v3, 1/3),
        Edge(v3, v2, 1/2),
        Edge(v3, v1, 1/2)
    }
)

dtmc3: mc.DTMC = mc.DTMC(
    {v1, v2, v3, v4},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 0.75),
        Edge(v3, v4, 0.25),
        Edge(v4, v4, 1)
    }
)

dtmc4: mc.DTMC = mc.DTMC(
    {v1, v2},
    {
        Edge(v1, v2, 1),
        Edge(v2, v1, 1)
    }
)

dtmc5: mc.DTMC = mc.DTMC(
    {v1, v2, v3},
    {
        Edge(v1, v2, 0.5),
        Edge(v1, v3, 0.5),
        Edge(v2, v2, 1),
        Edge(v3, v3, 1)
    }
)


# TEST: trace_n_step_futures
assert dtmc1.trace_n_step_futures(v1, 0) == {(v1,)}
assert dtmc1.trace_n_step_futures(v1, 1) == {(v1, v2)}
assert dtmc1.trace_n_step_futures(v1, 4) == {(v1, v2, v3, v1, v2)}
assert dtmc2.trace_n_step_futures(v1, 2) == {(v1, v2, v2), (v1, v2, v3)}
assert dtmc2.trace_n_step_futures(v3, 2) == {(v3, v1, v2), (v3, v2, v2), (v3, v2, v3)}
assert dtmc2.trace_n_step_futures(v1, 3) == {(v1, v2, v2, v2), (v1, v2, v2, v3), (v1, v2, v3, v1), (v1, v2, v3, v2)}

# TEST: run_dtmc
assert dtmc1.run(v1, 0) == (v1,)
assert dtmc1.run(v2, 0) == (v2,)
assert dtmc1.run(v1, 1) == (v1, v2)
assert dtmc1.run(v1, 9) == (v1, v2, v3, v1, v2, v3, v1, v2, v3, v1)
assert dtmc2.run(v1, 0) == (v1,)
for i in range(16):
    assert dtmc2.run(v1, i) in dtmc2.trace_n_step_futures(v1, i)
    assert dtmc2.run(v2, i) in dtmc2.trace_n_step_futures(v2, i)
    assert dtmc2.run(v3, i) in dtmc2.trace_n_step_futures(v3, i)

    assert dtmc3.run(v1, i) in dtmc3.trace_n_step_futures(v1, i)
    assert dtmc3.run(v2, i) in dtmc3.trace_n_step_futures(v2, i)
    assert dtmc3.run(v3, i) in dtmc3.trace_n_step_futures(v3, i)
    assert dtmc3.run(v4, i) in dtmc3.trace_n_step_futures(v4, i)

# TEST: trace_n_step_transition_probability
assert dtmc1.trace_n_step_transition_probability(v1, v1, 1) == 0
assert dtmc1.trace_n_step_transition_probability(v1, v2, 1) == 1
assert dtmc1.trace_n_step_transition_probability(v1, v1, 36) == 1
assert isclose(dtmc2.trace_n_step_transition_probability(v2, v3, 1), 1/3)
assert isclose(dtmc2.trace_n_step_transition_probability(v2, v1, 2), 1/6)
assert isclose(dtmc2.trace_n_step_transition_probability(v2, v2, 2), 11/18)

# TEST: trace_period
assert dtmc1.trace_period(v1) == 3
assert dtmc1.trace_period(v2) == 3
assert dtmc1.trace_period(v3) == 3
assert dtmc2.trace_period(v1) == 1
assert dtmc2.trace_period(v2) == 1
assert dtmc2.trace_period(v3) == 1
assert dtmc3.trace_period(v1) == 3
assert dtmc3.trace_period(v2) == 3
assert dtmc3.trace_period(v3) == 3
assert dtmc3.trace_period(v4) == 1
assert dtmc4.trace_period(v1) == 2
assert dtmc4.trace_period(v2) == 2

# TEST: classify_states
assert dtmc1.classify_states() == frozenset({frozenset({v1, v2, v3})})
assert dtmc2.classify_states() == frozenset({frozenset({v1, v2, v3})})
assert dtmc3.classify_states() == frozenset({frozenset({v1, v2, v3}), frozenset({v4})})
assert dtmc4.classify_states() == frozenset({frozenset({v1, v2})})
assert dtmc5.classify_states() == frozenset({frozenset({v1}), frozenset({v2}), frozenset({v3})})

# TEST: irreducible
assert dtmc1.is_irreducible() == True
assert dtmc2.is_irreducible() == True
assert dtmc3.is_irreducible() == False
assert dtmc4.is_irreducible() == True
assert dtmc5.is_irreducible() == False

# TEST: aperiodic
assert dtmc1.is_aperiodic(v1) == False
assert dtmc2.is_aperiodic(v1) == True
assert dtmc3.is_aperiodic(v1) == False
assert dtmc3.is_aperiodic(v4) == True
assert dtmc4.is_aperiodic(v1) == False

# TEST: is_closed
assert dtmc1.is_closed(ISet({v1, v2, v3})) == True
assert dtmc5.is_closed(ISet({v1})) == False

# TEST: is_transient
assert dtmc1.is_transient(ISet({v1, v2, v3})) == False

# TEST: hitting_probability
assert dtmc1.hitting_probability(v1, ISet({v2, v3})) == 1
assert dtmc1.hitting_probability(v1, ISet({v3})) == 1
assert dtmc2.hitting_probability(v3, ISet({v4})) == 1
assert dtmc5.hitting_probability(v1, ISet({v2,v3})) == 1
assert dtmc5.hitting_probability(v1, ISet({v2})) == 0.5

# TEST: expected_hitting_time
assert dtmc1.expected_hitting_time(v1, ISet({v3})) == 2
assert dtmc2.expected_hitting_time(v1, ISet({v4})) == 3

# TEST: exists_stationary_distribution

# TEST: find_stationary_distribution

# TEST: is_reversible