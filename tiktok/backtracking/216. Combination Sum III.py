class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, startIndex, record, res):
        if len(record) == k:
            if sum(record) == n:
                res.append(record[:])
            else:
                return

        if sum(record) > n:
            return

        for i in range(startIndex, 10):
            record.append(i)
            self.dfs(k, n, i+1, record, res)
            record.pop()
