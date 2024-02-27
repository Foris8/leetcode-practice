# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dict_ = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        res = []
        while queue:
            ele = queue.popleft()

            curr_node, val = ele

            dict_[val].append(curr_node.val)

            if curr_node.left:
                queue.append((curr_node.left, val - 1))
            if curr_node.right:
                queue.append((curr_node.right, val + 1))

        for i in (sorted(dict_.keys())):
            res.append(dict_[i])
        return res
