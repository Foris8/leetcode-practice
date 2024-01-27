class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        prev_diff = 0
        curr_diff = 0
        count = 1

        for i in range(len(nums)-1):
            curr_diff = nums[i+1] - nums[i]

            if (prev_diff <= 0 and curr_diff > 0) or (prev_diff >= 0 and curr_diff < 0):
                count += 1
                prev_diff = curr_diff

        return count
