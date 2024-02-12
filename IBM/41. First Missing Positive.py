class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i] > 0 and nums[i] != nums[nums[i] - 1]:

                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return nums[-1] + 1