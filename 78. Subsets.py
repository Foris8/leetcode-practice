class Solution:
    

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        self.dfs(nums,0,[],res)
        return res

    def dfs(self,nums,startIndex, current,res):

        if startIndex >= len(nums):
            return
        
        for i in range(startIndex, len(nums)):
            current.append(nums[i])
            res.append(current.copy())
            self.dfs(nums,i+1, current, res)
            current.pop()
        