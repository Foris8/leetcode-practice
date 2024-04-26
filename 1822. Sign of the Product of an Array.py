class Solution:
    def arraySign(self, nums: List[int]) -> int:

        prod = nums[0]

        for i in range(1, len(nums)):
            prod *= nums[i]

        if prod < 0:
            return -1
        elif prod == 0:
            return 0
        else:
            return 1
