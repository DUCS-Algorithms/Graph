
import numpy as np
import graph
from graph import Adj_Mat, Edge

if __name__ == "__main__":
    verts: list[str] = ['a', 'b', 'c']
    edges: list[Edge] = [('a','b'), ('c','a')]
    g = graph.GraphAM(verts)
    g.addEdges(edges)
    print('The verticies are ')
    print(*g.getV(), sep=',')
    print('The empty graph')
    print(g.getGraph())


