class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum_ = sum(nums)

        curr_sum = 0

        for i, num in enumerate(nums):

            if curr_sum == (sum_-curr_sum - num):
                return i
            curr_sum += num
        return -1
