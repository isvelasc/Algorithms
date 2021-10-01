
def max_degree(G):
    # Input: Graph
    # Output: Vertex with maximum degree

    MAX = 0
    maxDeg = None
    for v in G.values():
        if len(v.neighbors) > MAX:
            MAX = len(v.neighbors)
            maxDeg = v

    return maxDeg


def remove_adjacent(G, v):
    # Input: Graph G, Vertex v
    # Output: Graph with edges connected to v removed

    altGraph = G
    for adjacents in altGraph.values():
        if v.value in adjacents.neighbors:
            adjacents.neighbors.pop(v.value)

    altGraph.pop(v.value)
    return altGraph


def SGVC(G):
    # Input: Graph
    # Output: Vertex Cover

    vc = []
    altGraph = G
    while altGraph:
        currVertex = max_degree(altGraph)
        if not currVertex:
            break
        vc.append(currVertex.value)
        altGraph = remove_adjacent(altGraph, currVertex)

    print(*vc, sep=" ")
