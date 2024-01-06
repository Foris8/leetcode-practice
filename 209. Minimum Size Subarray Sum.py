class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_count = 100001
        left = 0
        right = 0
        size = len(nums)
        cur_sum = 0

        while right < size:
            cur_sum += nums[right]

            while cur_sum >= target:
                min_count = min(min_count, right - left+1)
                cur_sum -= nums[left]  # move left point
                left += 1

            right += 1

        return min_count
