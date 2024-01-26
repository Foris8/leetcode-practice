# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = collections.deque([root])  # deque([]) is initialized the queue
        res = []

        while queue:
            level = []

            for _ in range(len(queue)):
                # add element into queue
                new_ele = queue.popleft()

                if new_ele.left:
                    queue.append(new_ele.left)

                if new_ele.right:
                    queue.append(new_ele.right)

                level.append(new_ele.val)

            res.append(level)

        return res
