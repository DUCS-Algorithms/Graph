
import numpy as np
import graph
from graph import ADJ_MAT, EDGE

if __name__ == "__main__":
    verts: list[str] = ['a', 'b', 'c']
    edges: list[EDGE] = [('a','b'), ('c','a')]
    g = graph.GraphAM(verts, directed=True)
    g.addEdges(edges)
    print('The verticies are ')
    print(*g.getV(), sep=',')
    print('The empty graph')
    print(g.getGraph())

