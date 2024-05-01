class Solution:
    def __init__(self):
        self.result = []
        self.path = [0]

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        self.dfs(graph, 0)
        return self.result

    def dfs(self, graph, root):
        if root == len(graph) - 1:
            # deep copy
            self.result.append(self.path[:])
            return

        for node in graph[root]:
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop()
