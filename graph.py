# Module graph
# Author: S. Sigman    Date Created: 9/1/2022
#
# This module provides graph data structures. The following
# Graph representations are provided:
#    * GraphAM - graph stored  using an adjacency
#                matrix - the matrix is an numpy array
#    * GraphAL - graph stored using an adjacency list -
#                TO BE Implemented (9/1/2022)
#
# Modification Log:
#

import numpy as np
from nptyping import NDArray, Shape, Integer
from typing import Any

EDGE = tuple[str,str]
ADJ_MAT = NDArray[Shape['Any, ...'], Integer]

class GraphAM:
    def __init__(self, verts: list[str], edges: list[EDGE]=[], *, directed :bool=False, eleType='i') -> None:
        self.V :list[str] = verts
        self.directed :bool = directed
        self.graph :ADJ_MAT = np.zeros((len(verts),len(verts)), dtype=eleType)
        # add edges if any are specified
        if edges != []:
            for e in edges:
                # get index of start and end vertices
                start = self.V.index(e[0])
                end = self.V.index(e[1])
                # add directed edge
                self.graph[start,end] = 1
                # if undirected add symmetric edge
                if not self.directed:
                    self.graph[end,start] = 1


    # Method to return the set of verticies
    def getV(self) -> list[str]: 
        return(self.V)

    # Method to return the graph object
    def getGraph(self) -> ADJ_MAT:
        return(self.graph)

    # Method to add the list of edges to the graph
    def addEdges(self, edges :list[EDGE]):
        if edges != []:
            for e in edges:
                # get index of start and end vertices
                start = self.V.index(e[0])
                end = self.V.index(e[1])
                # add directed edge
                self.graph[start,end] = 1
                # if undirected add symmetric edge
                if not self.directed:
                    self.graph[end,start] = 1