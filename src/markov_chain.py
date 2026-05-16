from graph import *
from random import choices
from math import gcd, prod

# returns set of edges (i,j, w)
def get_transitions(dtmc: Graph, i: Vertex) -> frozenset[Edge]:
    return frozenset({e for e in dtmc.E if e.v1 == i})

# simulate the dtmc
# returns X_0, ..., X_n
def run_dtmc(dtmc: Graph, i_0: Vertex, n: int) -> tuple[Vertex]:
    i = i_0
    state_history: list[Vertex] = [i]

    for _ in range(n):
        transitions: list[Edge] = list(get_transitions(dtmc, i))
        if transitions != []:
            transition: Edge = choices(transitions, [t.weight for t in transitions], k=1)[0]
            i = transition.v2
        state_history.append(i)

    return tuple(state_history)

# we want to find every possible path of size n-steps from i
# returns the set of ALL valid futures {(X_0, ..., X_n), ...}
def trace_n_step_futures(dtmc: Graph, i: Vertex, n: int, history: tuple[Vertex] = ()) -> set[tuple[Vertex]]:
    paths: set[tuple[Vertex]] = set()

    history = history + (i,)

    # base case
    if n == 0: paths.add(history)
    # general case
    elif n > 0:
        transitions = get_transitions(dtmc, i)
        for t in transitions:
            paths.update(trace_n_step_futures(dtmc, t.v2, n-1, history))

    return paths

# 1 to 1 map from vertex pair to edge
def _get_edge(dtmc: Graph, i: Vertex, j: Vertex) -> Edge:
    for t in get_transitions(dtmc, i):
        if t.v2 == j: return t

# maps vertex paths to a tuple of edges
def _get_path_edges(dtmc: Graph, path: tuple[Vertex]) -> tuple[Edge]:
    return (_get_edge(dtmc, path[i], path[i+1]) for i in range(len(path) - 1))

# p^(n)_i,j
def trace_n_step_transition_probability(dtmc: Graph, i: Vertex, j: Vertex, n: int) -> float:
    return sum(
        # product of edge weights in {path edges}
        (prod((e.weight for e in p)) for p in
        # {path edges} in a vertex path
        {_get_path_edges(dtmc, p) for p in
        # subset of {vertex paths} in n steps that end in j
        {p for p in trace_n_step_futures(dtmc, i, n) if p[-1] == j}})
    )

# gcd(J_i) i.e. period
def trace_period(dtmc: Graph, i: Vertex) -> int:
    # known lower bound
    time = 3 * len(dtmc.V)
    J_i = frozenset({n for n in range(1, time) if trace_n_step_transition_probability(dtmc, i, i, n) > 0})
    
    return gcd(*J_i)

def is_aperiodic(dtmc: Graph, i: Vertex) -> bool:
    return trace_period(dtmc, i) == 1

# maps our dtmc to a set of communicating classes
def classify_states(dtmc: Graph) -> frozenset[frozenset[Vertex]]:
    def communicates(i: Vertex) -> frozenset[Vertex]:
        return frozenset({v for p in trace_n_step_futures(dtmc, i, len(dtmc.V)) for v in p})

    return frozenset(
        frozenset({j for j in communicates(i) if i in communicates(j)})
        for i in dtmc.V
    )

def is_irreducible(dtmc: Graph) -> bool:
    return classify_states(dtmc) == frozenset({dtmc.V})

def hitting_probability(dtmc: Graph, i: Vertex, A: frozenset[Vertex]) -> float:
    pass

def expected_hitting_time(dtmc: Graph, i: Vertex, A: frozenset[Vertex]) -> float:
    pass

def is_transient(dtmc: Graph, i: Vertex) -> bool:
    pass

def is_recurrent(dtmc: Graph, i: Vertex) -> bool:
    return not is_transient(dtmc, i)

def is_positive_recurrent(dtmc: Graph, i: Vertex) -> bool:
    pass

def is_null_recurrent(dtmc: Graph, i: Vertex) -> bool:
    return not is_positive_recurrent(dtmc, i)

def exists_stationary_distribution(dtmc: Graph) -> bool:
    pass

def find_stationary_distribution(dtmc: Graph) -> tuple[float]:
    pass

def is_reversible(dtmc: Graph) -> bool:
    pass