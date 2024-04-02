# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        stack = deque([root])

        while stack:
            length = len(stack)
            for _ in range(length):
                ele = stack.popleft()
                if ele.val != value:
                    return False

                if ele.left:
                    stack.append(ele.left)
                if ele.right:
                    stack.append(ele.right)

        return True
