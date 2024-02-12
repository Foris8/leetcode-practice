class Solution:
    def __init__(self):
        self.sum = 0
        self.tree = {}

    def pathSum(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        for num in nums:
            key = num // 10
            value = num % 10
            self.tree[key] = value

        self.traverse(nums[0] // 10, 0)

        return self.sum

    def traverse(self, root, preSum):
        level = root // 10
        pos = root % 10
        left = (level + 1) * 10 + pos * 2 - 1
        right = (level + 1) * 10 + pos * 2

        curSum = preSum + self.tree[root]

        if left not in self.tree and right not in self.tree:
            self.sum += curSum
            return

        if left in self.tree:
            self.traverse(left, curSum)
        if right in self.tree:
            self.traverse(right, curSum)
