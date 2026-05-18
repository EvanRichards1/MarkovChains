from graph import *
import markov_chain as mc
from visualise import visualise

v1: Vertex = Vertex('1')
v2: Vertex = Vertex('2')
v3: Vertex = Vertex('3')
v4: Vertex = Vertex('4')

dtmc1: Graph = Graph(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 1)
    },
    "dtmc1"
)

dtmc2 = Graph(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v2, v2, 2/3),
        Edge(v2, v3, 1/3),
        Edge(v3, v2, 1/2),
        Edge(v3, v1, 1/2)
    },
    "dtmc2"
)

dtmc3: Graph = Graph(
    {v1, v2, v3, v4},
    {
        Edge(v1, v2, 1),
        Edge(v2, v3, 1),
        Edge(v3, v1, 0.75),
        Edge(v3, v4, 0.25),
        Edge(v4, v4, 1)
    },
    "dtmc3"
)

dtmc4: Graph = Graph(
    {v1, v2},
    {
        Edge(v1, v2, 1),
        Edge(v2, v1, 1)
    },
    "dtmc4"
)

dtmc5: Graph = Graph(
    {v1, v2, v3},
    {
        Edge(v1, v2, 1),
        Edge(v1, v3, 1),
        Edge(v2, v2, 1),
        Edge(v3, v3, 1)
    },
    "dtmc5"
)