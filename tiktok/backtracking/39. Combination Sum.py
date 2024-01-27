class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if min(candidates) > target:
            return []

        res = []
        self.dfs(candidates, target, [], res, 0)
        return res

    def dfs(self, candidates, target, record, res, startIndex):
        if sum(record) > target:
            return

        if sum(record) == target:
            res.append(record[:])

        for i in range(startIndex, len(candidates)):
            record.append(candidates[i])
            self.dfs(candidates, target, record, res, i)
            record.pop()
