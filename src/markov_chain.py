from graph import *
from random import choices
from math import gcd, prod

def get_transitions(dtmc: Graph, state: Vertex):
    transitions: set[Edge] = set()

    for e in dtmc.E:
        if e.v1 == state: transitions.add(e)
    
    return transitions

# simulate the dtmc
def run_dtmc(dtmc: Graph, start_state: Vertex, steps: int) -> list[Vertex]:
    state: Vertex = start_state
    state_history: list[Vertex] = [state]

    for i in range(0, steps):
        transitions: list[Edge] = list(get_transitions(dtmc, state))
        if transitions != []:
            transition: Edge = choices(transitions, [t.weight for t in transitions], k=1)[0]
            state = transition.v2
        state_history.append(state)
    
    return state_history

# we want to find every possible path of size n-steps from i
def trace_n_step_transitions(dtmc: Graph, i: Vertex, n: int, history: tuple[Vertex] = ()) -> set[tuple[Vertex]]:
    state: Vertex = i
    paths: set[tuple[Vertex]] = set()

    history = history + (i,)

    # base case
    if n == 1:
        transitions = get_transitions(dtmc, i)
        for t in transitions:
            path: tuple[Vertex] = history + (t.v2,)
            paths.add(path)
    # general case
    elif n > 1:
        transitions = get_transitions(dtmc, i)
        for t in transitions:
            paths.update(trace_n_step_transitions(dtmc, t.v2, n-1, history))

    return paths

# 1 to 1 map
def _get_edge(dtmc: Graph, i: Vertex, j: Vertex) -> Edge:
    transitions = get_transitions(dtmc, i)

    for t in transitions:
        if t.v2 == j: return t

def _get_path_edges(dtmc: Graph, path: tuple[Vertex]) -> tuple[Edge]:
    edges: list[Edge] = []

    for i in range(0, len(path)-1):
        edges.append(_get_edge(dtmc, path[i], path[i+1]))

    return tuple(edges)

def trace_n_step_transition_probability(dtmc: Graph, i: Vertex, j: Vertex, n: int) -> float:
    all_transition_paths = trace_n_step_transitions(dtmc, i, n)

    transition_paths = {p for p in all_transition_paths if p[-1] == j}
    transition_paths_edges: set[tuple[Edge]] = {_get_path_edges(dtmc, p) for p in transition_paths}
    path_weights = {prod((e.weight for e in p)) for p in transition_paths_edges}

    return sum(path_weights)

def trace_period(dtmc: Graph, i: Vertex) -> int:
    # known lower bound
    time = 3 * len(dtmc.V)

    J_i: set[int] = set()

    for j in range(1, time):
        if trace_n_step_transition_probability(dtmc, i, i, j) > 0: J_i.add(j)
    
    return gcd(*J_i)