from graphviz import Digraph
from graph import DTMC

# This is just a quick peripheral procedure to visualise my diraphs 
def visualise(g: DTMC, f: str = None, e: str = "png", view: bool = False) -> None:
    if not f:
        f = g.label
    
    d = Digraph(g.label, graph_attr={"dpi" : "300", "rankdir" : "LR"})

    for edge in g.E:
        d.edge(edge.v1.label, edge.v2.label, label=str(edge.weight))
    
    d.render(f, view=view, format=e, cleanup=True)