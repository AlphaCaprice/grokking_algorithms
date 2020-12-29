import pytest

from grokking_algorithms.chapter7.graph_short_path import dijkstra


graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {},
    "c": {},
}


@pytest.mark.parametrize(
    ["start", "end", "result"],
    [
        ("start", "fin", "start -> b -> a -> fin"),
        ("start", None, {"a": 5, "b": 2, "c": float("inf"), "fin": 6, "start": 0}),
        ("start", "c", "c node is unreachable"),
    ],
)
def test_handshakes_bfs(start, end, result):
    assert dijkstra(graph, start, end) == result
