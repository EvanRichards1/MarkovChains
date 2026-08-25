from graph import Graph, Vertex, Edge
from random import choices
from math import gcd, prod

class DTMC(Graph):
    # returns set of edges (i,j, w)
    def get_transitions(self, i: Vertex) -> frozenset[Edge]:
        return frozenset({e for e in self.E if e.v1 == i})

    # simulate the DTMC
    # returns X_0, ..., X_n
    def run(self, i_0: Vertex, n: int) -> tuple[Vertex]:
        i = i_0
        state_history: list[Vertex] = [i]

        for _ in range(n):
            transitions: list[Edge] = list(self.get_transitions(i))
            if transitions != []:
                transition: Edge = choices(transitions, [t.weight for t in transitions], k=1)[0]
                i = transition.v2
            state_history.append(i)

        return tuple(state_history)

    # we want to find every possible path of size n-steps from i
    # returns the set of ALL valid futures {(X_0, ..., X_n), ...}
    def trace_n_step_futures(self, i: Vertex, n: int, history: tuple[Vertex] = ()) -> frozenset[tuple[Vertex]]:
        paths: set[tuple[Vertex]] = set()

        history = history + (i,)

        # base case
        if n == 0:
            paths.add(history)
        # general case
        elif n > 0:
            transitions = self.get_transitions(i)
            for t in transitions:
                paths.update(self.trace_n_step_futures(t.v2, n-1, history))

        return frozenset(paths)

    # 1 to 1 map from vertex pair to edge
    def _get_edge(self, i: Vertex, j: Vertex) -> Edge:
        for t in self.get_transitions(i):
            if t.v2 == j:
                return t

    # maps vertex paths to a tuple of edges
    def _get_path_edges(self, path: tuple[Vertex]) -> tuple[Edge]:
        return (self._get_edge(path[i], path[i+1]) for i in range(len(path) - 1))

    # p^(n)_i,j
    def trace_n_step_transition_probability(self, i: Vertex, j: Vertex, n: int) -> float:
        # Find paths that end in j
        valid_vertex_paths = {p for p in self.trace_n_step_futures(i, n) if p[-1] == j}
        valid_paths = {self._get_path_edges(p) for p in valid_vertex_paths}
        # Sum the product of edge weights
        probability = sum(prod(e.weight for e in p) for p in valid_paths)

        return probability

    # gcd(J_i) i.e. period
    def trace_period(self, i: Vertex) -> int:
        # known lower bound
        time = 3 * len(self.V)
        J_i = {n for n in range(1, time) if self.trace_n_step_transition_probability(i, i, n) > 0}
        
        return gcd(*J_i)

    # period 1
    def is_aperiodic(self, i: Vertex) -> bool:
        return self.trace_period(i) == 1

    # maps our self to a set of communicating classes
    def classify_states(self) -> frozenset[frozenset[Vertex]]:
        def communicates(i: Vertex) -> frozenset[Vertex]:
            return frozenset({v for p in self.trace_n_step_futures(i, len(self.V)) for v in p})

        return frozenset(
            frozenset({j for j in communicates(i) if i in communicates(j)})
            for i in self.V
        )

    # i.e. 1 communicating class C=S
    def is_irreducible(self) -> bool:
        return self.classify_states() == {self.V}

    def is_closed(self, C: frozenset[Vertex]) -> bool:
        return {e for e in self.E if e.v1 in C and e.v2 not in C} == set()

    def hitting_probability(self, i: Vertex, A: frozenset[Vertex]) -> float:
        pass

    def expected_hitting_time(self, i: Vertex, A: frozenset[Vertex]) -> float:
        pass

    def is_transient(self, C: frozenset[Vertex]) -> bool:
        return not self.is_closed(C)

    def is_recurrent(self, C: frozenset[Vertex]) -> bool:
        return not self.is_transient(i)

    def is_positive_recurrent(self, i: Vertex) -> bool:
        pass

    def is_null_recurrent(self, i: Vertex) -> bool:
        return not self.is_positive_recurrent(i)

    def exists_stationary_distribution(self) -> bool:
        pass

    def find_stationary_distribution(self) -> tuple[float]:
        pass

    def is_reversible(self) -> bool:
        pass

    def __repr__(self) -> str:
        communicating_classes = self.classify_states()

        return (
f"""Sample run: {self.run(next(iter(self.V)), 15)}
Communicating classes: {communicating_classes}
{"Irreducible" if self.is_irreducible() else "Reducible"}
Periodicities:
{'\n'.join((f"- {c}: {self.trace_period(next(iter(c)))}" for c in communicating_classes))}"""
        )
        # return f"""
        #     Sample run: {run_self(self, next(iter(self.V)), 15)}
        #     Communicating classes: {communicating_classes}
        #     {"Irreducible" if is_irreducible(self) else "Reducible"}
        #     Periodicities:
        #     {'\n'.join((f"\t- {c}: {trace_period(self, next(iter(c)))}" for c in communicating_classes))}
        #     Transience/Recurrence:
        #     {'\n'.join((f"\t- {c}: {"Transient" if is_transient(next(iter(c))) else "Recurrent"}" for c in communicating_classes))}
        #     Positive/Null Recurrence:
        #     {'\n'.join((f"\t- {c}: {"Positive Recurrent" if is_positive_recurrent(next(iter(c))) else "Null Recurrent"}" for c in {c for c in communicating_classes if is_recurrent(next(iter(c)))}))}
        # """