import sys
from copy import deepcopy as dcp
from dataclasses import dataclass, field
from smart_greedy_vertex_cover import *
from basic_greedy_vertex_cover import *
from brute_force_vertex_cover import *


@dataclass
class Vertex:
    value: int
    neighbors: dict() = field(default_factory=dict)


def handle_input(input):
    graph = dict()

    for items in input.readlines():
        x, y = items.strip("\n").split(" ")
        x = int(x)
        y = int(y)
        v1 = graph.get(x)
        v2 = graph.get(y)

        if not v1:
            graph[x] = Vertex(x, {y: None})
        else:
            if not y in v1.neighbors:
                v1.neighbors[y] = None

        if not v2:
            graph[y] = Vertex(y, {x: None})
        else:
            if not x in v2.neighbors:
                v2.neighbors[x] = None

    return graph


def main(argv):
    input = open(argv[1], "r")
    graph = handle_input(input)
    SGVC(dcp(graph))
    BGVC(dcp(graph))
    BFVC(graph)
    input.close()


if __name__ == "__main__":
    main(sys.argv)
