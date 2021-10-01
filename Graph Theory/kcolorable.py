import sys
from dataclasses import dataclass, field


@dataclass(order=True)
class Vertex:
    value: int
    neighbors: dict() = field(default_factory=dict)
    discovered: bool = False
    color: int = 0


def handle_input(input):
    graph = dict()

    for items in input.readlines():
        x, y = items.strip("\n").split(", ")
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


def is_colorable(graph):
    colors = []
    count = 2

    for v in graph.values():
        colorable = True
        if not v.discovered:
            colors.append([])
            colors.append([])
            colorable = explore(graph, v, 1, colors, count)
            count += 2
        if not colorable:
            print("Is not 2-colorable.")
            return

    for color_set in colors:
        color_set.sort()
    colors.sort()

    print("Is 2-colorable:")
    for sets in colors:
        print(*sets, sep=", ")


def explore(graph, v, color, colors, count):
    v.discovered = True
    v.color = color

    if color == 1:
        colors[count - 2].append(v.value)
    else:
        colors[count - 1].append(v.value)

    for neighbor in v.neighbors:
        u = graph.get(neighbor)
        if not u.discovered:
            colorable = explore(graph, u, -color, colors, count)
            if not colorable:
                return False
        elif u.discovered and u.color == v.color:
            return False

    return True


def main(argv):
    input = open(argv[1], "r")
    graph = handle_input(input)
    is_colorable(graph)
    input.close()


if __name__ == "__main__":
    main(sys.argv)
