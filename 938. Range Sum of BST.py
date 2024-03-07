# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        queue = deque()
        queue.append(root)

        while queue:
            ele = queue.popleft()

            if ele.val >= low and ele.val <= high:
                res += ele.val

            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)

        return res
