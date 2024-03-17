class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        arr_set = [0] * n

        for ele in nums:
            arr_set[ele-1] += 1

            if arr_set[ele-1] >= 2:
                return ele
