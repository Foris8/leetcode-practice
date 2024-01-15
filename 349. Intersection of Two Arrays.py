class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001

        for i in nums1:
            count1[i] = 1

        for j in nums2:
            count2[j] = 1

        res = []
        for i in range(1001):
            if count1[i] == 1 and count2[i] == 1:
                res.append(i)

        return res
