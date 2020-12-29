from typing import Union, Dict

graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {},
    "c": {},
}


def find_lowest_cost_node(costs: dict, visited: set) -> Union[str, None]:
    lowest_cost = float("inf")
    lowest_node = None
    for node, cost in costs.items():
        if node not in visited and cost < lowest_cost:
            lowest_node = node
            lowest_cost = cost
    return lowest_node


def dijkstra(graph: dict, start: str, end=None) -> Union[str, dict]:
    """Shortest path between 2 nodes if end is given,
    dict with shortest paths for all nodes otherwise
    """
    nodes_cost = dict.fromkeys(graph.keys(), float("inf"))
    nodes_parents: Dict[str, Union[str, None]] = dict.fromkeys(graph.keys(), None)
    visited = set()

    nodes_cost[start] = 0
    curr_node = start
    while curr_node:
        cost = nodes_cost[curr_node]

        for child, value in graph[curr_node].items():
            if child not in visited:
                curr_cost = value + cost
                if nodes_cost[child] > curr_cost:
                    nodes_cost[child] = curr_cost
                    nodes_parents[child] = curr_node

        visited.add(curr_node)
        curr_node = find_lowest_cost_node(nodes_cost, visited)  # type: ignore

    if end:
        if nodes_cost[end] == float("inf"):
            return f"{end} node is unreachable"
        path = []
        node = end
        while parent := nodes_parents[node]:  # type: ignore
            path.append(node)
            node = parent
        path.append(start)

        return " -> ".join(reversed(path))

    return nodes_cost


if __name__ == "__main__":
    print(dijkstra(graph, "start", "fin"))
    print(dijkstra(graph, "start", "c"))
