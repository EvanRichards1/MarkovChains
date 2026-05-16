from graph import *
import markov_chain as mc

va: Vertex = Vertex('a')
vb: Vertex = Vertex('b')
vc: Vertex = Vertex('c')

dtmc1 = Graph(
    {va, vb, vc},
    {
        Edge(va, vb, 1),
        Edge(vb, vb, 2/3),
        Edge(vb, vc, 1/3),
        Edge(vc, vb, 1/2),
        Edge(vc, va, 1/2)
    }
)

dtmc2 = Graph(
    {va, vb, vc},
    {
        Edge(va, vb, 1/2),
        Edge(va, vc, 1/2)
    }
)

dtmc3 = Graph(
    {va, vb, vc},
    {
        Edge(va, vb, 1),
        Edge(vb, vc, 1),
        Edge(vc, va, 1)
    }
)

print(f"dtmc3 communication classes? {mc.classify_states(dtmc3)}")
print(f"dtmc2 communication classes? {mc.classify_states(dtmc2)}")
print(f"dtmc1 communication classes? {mc.classify_states(dtmc1)}")