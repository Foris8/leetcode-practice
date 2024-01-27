# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            level = []

            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(level[-1].val)

        return res
