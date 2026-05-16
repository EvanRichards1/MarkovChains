from graph import *
import markov_chain as mc

v1 = Vertex('1')
v2 = Vertex('2')
v3 = Vertex('3')
v4 = Vertex('4')

dtmc1: Graph = Graph(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 1)
    }
)

dtmc2 = Graph(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v2, 2/3),
        Edge(v2, v3, 1/3),
        Edge(v3, v2, 1/2),
        Edge(v3, v1, 1/2)
    }
)

# TEST: trace_n_step_futures
assert mc.trace_n_step_futures(dtmc1, v1, 0) == {(v1,)}
assert mc.trace_n_step_futures(dtmc1, v1, 1) == {(v1, v2)}
assert mc.trace_n_step_futures(dtmc1, v1, 4) == {(v1, v2, v3, v1, v2)}
assert mc.trace_n_step_futures(dtmc2, v1, 2) == {(v1, v2, v2), (v1, v2, v3)}
assert mc.trace_n_step_futures(dtmc2, v3, 2) == {(v3, v1, v2), (v3, v2, v2), (v3, v2, v3)}
assert mc.trace_n_step_futures(dtmc2, v1, 3) == {(v1, v2, v2, v2), (v1, v2, v2, v3), (v1, v2, v3, v1), (v1, v2, v3, v2)}

# TEST: run_dtmc
assert mc.run_dtmc(dtmc1, v1, 0) == (v1,)
assert mc.run_dtmc(dtmc1, v2, 0) == (v2,)
assert mc.run_dtmc(dtmc1, v1, 1) == (v1, v2)
assert mc.run_dtmc(dtmc1, v1, 9) == (v1, v2, v3, v1, v2, v3, v1, v2, v3, v1)
assert mc.run_dtmc(dtmc2, v1, 0) == (v1,)
for i in range(16):
    assert mc.run_dtmc(dtmc2, v1, i) in mc.trace_n_step_futures(dtmc2, v1, i)
    assert mc.run_dtmc(dtmc2, v2, i) in mc.trace_n_step_futures(dtmc2, v2, i)
    assert mc.run_dtmc(dtmc2, v3, i) in mc.trace_n_step_futures(dtmc2, v3, i)
    