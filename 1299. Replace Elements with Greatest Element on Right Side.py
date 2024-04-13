class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ele = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(max_ele, arr[i])
            arr[i] = max_ele

            max_ele = newMax

        return arr
