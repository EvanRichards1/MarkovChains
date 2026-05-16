class Vertex:
    def __init__(self, label: str):
        self.label = label
    
    def __repr__(self):
        return f"({self.label})"

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, weight: float):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    
    def __repr__(self):
        return f"{self.v1} ->{self.weight} {self.v2}"

class Graph:
    def __init__(self, V: frozenset[Vertex], E: frozenset[Edge]):
        self.V = frozenset(V)
        self.E = frozenset(E)
    
    def __repr__(self):
        return f"Graph:\n\tVertices: {self.V}\n\tEdges: {self.E}"