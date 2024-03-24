# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.trasversal(root)
        return max(dp)

    def trasversal(self, node):
        # if node is empty
        if not node:
            return (0, 0)

        # left
        # right

        left = self.trasversal(node.left)
        right = self.trasversal(node.right)

        # not rob current node:
        val_1 = node.val + left[0] + right[0]

        val_0 = max(left[0], left[1]) + max(right[0], right[1])

        return (val_0, val_1)
