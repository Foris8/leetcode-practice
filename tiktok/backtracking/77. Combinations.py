class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        record = []
        res = []
        self.dfs(n, k, 1, record, res)
        return res

    def dfs(self, n, k, startIndex, record, res):

        # stop condition
        if len(record) == k:
            res.append(record[:])  # shallow copy

        for i in range(startIndex, n+1):
            record.append(i)
            self.dfs(n, k, i+1, record, res)
            record.pop()  # backtracking
