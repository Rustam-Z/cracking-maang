# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Solution:
          What if we imagine the tree as a graph. 
          Should we use BFS or DFS, or something modified. 
            - We should use BFS. And count time which is the number of levels.           
        """
      
        graph = self.convert_tree_to_graph(root)
        visited = {start}  # Set for visited nodes.
        queue = deque([(start, 0)])  # Queue for nodes to visit.
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(time, max_time)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, time + 1))

        return max_time

    @staticmethod
    def convert_tree_to_graph(root) -> dict:
        graph = defaultdict(set)
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)): 
                parent = queue.popleft()

                if parent.left is not None:
                    queue.append(parent.left)
                    graph[parent.val].add(parent.left.val)

                if parent.right is not None:
                    queue.append(parent.right)
                    graph[parent.val].add(parent.right.val)

        # Make graph undirected. 
        graph_ = defaultdict(set)
        for node, neighbors in graph.items():
            graph_[node].update(neighbors)
            for neighbor in neighbors:
                graph_[neighbor].add(node)

        return graph_
