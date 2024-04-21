class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        vis = [False] * n
        return self.dfs(source, graph, vis, destination)

    def dfs(self, node, graph, vis, destination):
        if node == destination:
            return True 
            
        vis[node] = True
        for neighbor in graph[node]:
            if not vis[neighbor]:
                if self.dfs(neighbor, graph, vis, destination):
                    return True
        return False
