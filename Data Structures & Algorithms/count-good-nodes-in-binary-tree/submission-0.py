# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maxValue):
            if not curr:
                return 0
            maxValue = max(maxValue, curr.val)
            if curr.val >= maxValue:
                print(curr.val)
                return dfs(curr.left, maxValue) + dfs(curr.right, maxValue) + 1
            else:
                return dfs(curr.left, maxValue) + dfs(curr.right, maxValue)

        return dfs(root, root.val)

