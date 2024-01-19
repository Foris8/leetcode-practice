class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # 去重
                continue

            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1

                if j > i+1 and nums[j] == nums[j-1]:  # 去重
                    continue

                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum_ > target:
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # check if the left and right pointer is the same as previous one after moving

                        while right > left and nums[right] == nums[right-1]:
                            right -= 1

                        while right > left and nums[left] == nums[left + 1]:
                            left += 1

                        left += 1
                        right -= 1

        return res
