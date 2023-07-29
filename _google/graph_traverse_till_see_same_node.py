"""
Input: Given a graph
    {
        [A: B, C, D],
        [B: C, D],
        [C: D, A],
        [D: A, B]
    }

If you were to choose a node, say A, output should be either A,B,C,D,A or A,C,D,A or A,D,A or A,D,B,C,D etc.
You continue traversing graph till you encounter same node again.
"""


def solution(graph: dict) -> list:
    result = []

    def backtrack(start, end, path, visited):
        if end in graph[path[-1]]:  # If end is in the neighbors of the last node in path.
            if len(path + end) > len(set(path + end)):
                result.append(path + end)

        for neighbor in graph[start]:
            if neighbor not in visited:
                visited.add(neighbor)
                backtrack(neighbor, end, path + neighbor, visited)
                visited.remove(neighbor)

    for key in graph:
        backtrack("A", key, "A", {"A"})

    return result


if __name__ == "__main__":
    graph = {"A": ["B", "C", "D"], "B": ["C", "D"], "C": ["D", "A"], "D": ["A", "B"]}
    print(solution(graph))

