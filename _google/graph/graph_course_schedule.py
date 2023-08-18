"""
Problem:
    You have to take N number of courses. Some courses have prerequisites. You can only take a course if you have
    completed its prerequisites. Find if you can complete all the courses.

Questions to ask:
    1. All courses have prerequisites? NO. Some courses don't have prerequisites.
    2. Should i finish all courses OR need to finish only N number of courses? Finish all courses.
    3. N starts from 0 or 1? 0
"""
from collections import defaultdict


def can_take_all_courses(N: int, prerequisites: list) -> bool:
    """
    Algorithm:
        1. Create a graph with N nodes.
        2. For each course, do a DFS and check if there is a cycle. If there is a cycle then we cannot complete all.

    Time: O(N^2)
    Space: O(N)

    EXAMPLE:
        [0, 1] [0, 2] [1, 3] [1, 4] [3, 4]
        0 -> 1, 2
        1 -> 3, 4
        2 -> []
        3 -> 4
        4 -> []

        0 -> 1 -> 3 -> 4
        0 -> 1 -> 4
        0 -> 2

    EXAMPLE:
        5
        [[1,4],[2,4],[3,1],[3,2]]
        1 -> 4
        2 -> 4
        3 -> 1, 2
        4 -> []
    """
    graph = defaultdict(list)
    for course, prerequisite in prerequisites:
        graph[course].append(prerequisite)

    def dfs(course: int, visited: set) -> bool:
        if course in visited:  # Cycle
            return False

        visited.add(course)  # Mark the current node as visited
        for prerequisite in graph[course]:  # Recursion for all the vertices adjacent to this vertex
            if dfs(prerequisite, visited) is False:
                return False

        # visited.remove(course)  # Remove the current node from the visited set, why? Because we are going to check for another path.
        return True

    for course in range(N):
        if dfs(course, visited=set()) is False:
            return False

    return True


def order_of_courses_to_take(N: int, prerequisites: list) -> list:
    """
    Problem: Return the order of courses to be taken.

    Questions:
        - What if I have the node which can go to multiple nodes? In which order should I take the nodes?

    Algorithm:
        - Create a graph.
        - Do a DFS and store the nodes in a stack.
        - Return the stack.

    Time: O(N^2)
    Space: O(N)
    """
    # Create a graph
    graph = defaultdict(list)
    for course, prerequisite in prerequisites:
        graph[course].append(prerequisite)

    # Do a DFS and store the nodes in a stack
    stack = []
    visited = set()

    def dfs(course: int) -> None:
        if course in visited:
            return

        visited.add(course)
        for prerequisite in graph[course]:
            dfs(prerequisite)

        stack.append(course)

    for course in range(N):
        dfs(course)

    return stack
