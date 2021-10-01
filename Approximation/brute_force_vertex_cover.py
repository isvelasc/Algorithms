import itertools
from copy import deepcopy as dcp
from smart_greedy_vertex_cover import *
from basic_greedy_vertex_cover import *


def possible_subsets(G):
    # Input: Graph
    # Output: The set of possible vertex covers

    vertices = list(G.keys())
    subsets = []
    for reps in range(0, len(vertices) + 1):
        for sub in itertools.combinations(vertices, reps):
            if not sub:
                continue
            subsets.append(list(sub))

    return subsets


def BFVC(G):
    # Input: Graph
    # Output: Vertex Cover

    subsets = possible_subsets(G)

    for vsets in subsets:
        altGraph = dcp(G)
        for v in vsets:
            vertex = altGraph.get(v)
            if not vertex:
                continue
            altGraph = remove_adjacent(altGraph, vertex)
            altGraph = prune_graph(altGraph)

        if not altGraph:
            print(*vsets, sep=" ")
            break
