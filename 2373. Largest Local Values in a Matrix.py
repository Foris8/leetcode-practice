class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        max_local = [[0] * (N - 2) for _ in range(N - 2)]

        for i in range(N-2):
            for j in range(N-2):
                max_local[i][j] = self.findMax(grid, i, j)

        return max_local

    def findMax(self, grid, x, y):
        max_ele = 0
        for i in range(x, x+3):
            for j in range(y, y+3):
                max_ele = max(max_ele, grid[i][j])

        return max_ele
