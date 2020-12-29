import pytest

from grokking_algorithms.chapter6.BFS import handshakes_bfs


people_graph = {
    "Mark": ["Ron", "Alice", "Marry"],
    "Ron": ["Alex", "Alice"],
    "Alice": [],
    "Marry": ["Ron", "Alex"],
    "Alex": ["Jerry"],
    "Jerry": ["Brad"],
    "Brad": [],
}


@pytest.mark.parametrize(
    ["start", "end", "handshakes", "result"],
    [
        ("Mark", "Alice", 1, True),
        ("Mark", "Alex", 1, False),
        ("Mark", "Jerry", 2, False),
        ("Mark", "Jerry", 3, True),
        ("Mark", "Brad", 3, False),
    ],
)
def test_handshakes_bfs(start, end, handshakes, result):
    assert handshakes_bfs(people_graph, start, end, handshakes) == result
