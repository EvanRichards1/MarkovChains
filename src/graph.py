# remove the ugly frozenset prepend for repr
class ISet(frozenset):
    def __repr__(self):
        return str(set(self))
    
    def __str__(self):
        return str(set(self))

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
    def __init__(self, V: ISet[Vertex], E: ISet[Edge], label: str = None):
        self.V = ISet(V)
        self.E = ISet(E)
        self.label = label
    
    def __repr__(self):
        return f"Graph:\n\tVertices: {self.V}\n\tEdges: {self.E}"