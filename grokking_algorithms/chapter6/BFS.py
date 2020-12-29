from collections import deque


def handshakes_bfs(people_graph: dict, start: str, end: str, handshakes: int) -> bool:
    """Checks if there are a connection between 2 people for given
    number of handshakes"""
    searched = set()
    search_queue = deque(people_graph[start])
    layer_len = len(search_queue)
    total_len = 0

    while handshakes and search_queue:
        value = search_queue.popleft()
        layer_len -= 1

        if value not in searched:
            if value == end:
                return True
            searched.add(value)
            search_queue.extend(people_graph[value])
            total_len += len(people_graph[value])

        if layer_len == 0:
            handshakes -= 1
            layer_len, total_len = total_len, 0
    return False
