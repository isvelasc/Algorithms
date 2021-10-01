from smart_greedy_vertex_cover import *
import random


def edge_pair(G):
    # Input: Graph
    # Output: Random edge

    k = G.get(random.choice(list(G.keys())))
    j = G.get(random.choice(list(k.neighbors.keys())))
    return [k, j]


def prune_graph(G):
    # Input: Graph
    # Output: A graph stripped of any vertex which has no edges

    tg = {}
    for v in G.values():
        if v.neighbors:
            tg[v.value] = v

    return tg


def BGVC(G):
    # Input: Graph
    # Output: Vertex Cover

    vc = []
    altGraph = G

    while altGraph:
        v, u = edge_pair(altGraph)
        vc.append(v.value)
        vc.append(u.value)
        altGraph = remove_adjacent(altGraph, v)
        altGraph = remove_adjacent(altGraph, u)
        altGraph = prune_graph(altGraph)

    print(*vc, sep=" ")
