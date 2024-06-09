class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for course, precourse in prerequisites:
            graph[precourse].append(course)

        in_degree = [0] * numCourses

        for course, precourse in prerequisites:
            in_degree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        res = []

        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) < numCourses:
            return []
        return res
