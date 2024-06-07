# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        path = collections.defaultdict(int)

        def dfs(root, path):
            if not root:
                return

            path[root.val] += 1

            if not root.left and not root.right:
                if self.palindromicCheck(path):
                    self.count += 1
            else:

                # check left
                dfs(root.left, path)
                dfs(root.right, path)
            path[root.val] -= 1

        dfs(root, path)

        return self.count

    def palindromicCheck(self, path):
        odd_check = False

        for k, v in path.items():
            if v % 2 == 1:
                if odd_check:
                    return False
                odd_check = True

        return True
