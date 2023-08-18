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
    """
    Algorithm:
        - Create a list of all possible paths.
        - Iterate through the graph and traverse the graph till you encounter the same node again.
    Time: O(n^2)
    Space: O(n^2)
    """

    result = []

    def backtrack(start, end, path, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)  # Mark the current node as visited

        if end in graph[path[-1]]:  # If end is in the neighbors of the last node in path.
            # if len(path + end) > len(set(path + end)):
            result.append(path + end)

        for neighbor in graph[start]:
            if neighbor not in visited:
                backtrack(neighbor, end, path + neighbor, visited)
                visited.remove(neighbor)  # Why? Because we are backtracking. We need to remove the node from visited.

    # Not necessarily A should be visited again. Can be any node.
    for key in graph:
        backtrack("A", key, "A")

    return result


if __name__ == "__main__":
    graph = {"A": ["B", "C", "D"], "B": ["C", "D"], "C": ["D", "A"], "D": ["A", "B"]}
    # ['ABCA', 'ABCDA', 'ABDA', 'ACA', 'ACDA', 'ADA', 'ADBCA', 'ABCDB', 'ABDB', 'ACDBC', 'ACDBD', 'ADBD', 'ADBCD']
    print(solution(graph))

