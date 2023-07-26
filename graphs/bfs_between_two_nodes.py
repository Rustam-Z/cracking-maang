from collections import deque


def bfs(graph, src, tgt):
    """Return the shortest path from the source (src) to the target (tgt) in the graph"""

    parents = {src: None}
    queue = deque([src])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)

                # CUSTOM
                if node == tgt:
                    break

    path = deque([tgt])
    while parents[tgt] is not None:
        path.appendleft(parents[tgt])
        tgt = parents[tgt]

    return list(path)


test = {
    "a": ["b", "f"],
    "b": ["a", "c", "g"],
    "c": ["b", "d", "g", "l"],
    "d": ["c", "e", "k"],
    "e": ["d", "f"],
    "f": ["a", "e"],
    "g": ["b", "c", "h", "l"],
    "h": ["g", "i"],
    "i": ["h", "j", "k"],
    "j": ["i", "k"],
    "k": ["d", "i", "j", "l"],
    "l": ["c", "g", "k"],
}

assert bfs(test, "a", "e") == ['a', 'f', 'e']
assert bfs(test, "a", "i") == ['a', 'b', 'g', 'h', 'i']
assert bfs(test, "a", "l") == ['a', 'b', 'c', 'l']
assert bfs(test, "b", "k") == ['b', 'c', 'd', 'k']
