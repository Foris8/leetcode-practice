# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val=val, left=root)
            return new_node

        queue = deque([root])
        curr_depth = 1

        while queue:

            curr_depth += 1
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                if curr_depth == depth:

                    new_node = TreeNode(val=val, left=curr_node.left)
                    curr_node.left = new_node

                    new_node = TreeNode(val=val, right=curr_node.right)
                    curr_node.right = new_node

                else:
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)

        return root
