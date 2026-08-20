# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(curr):
            if not curr:
                return 0
            
            leftMax = max(0, dfs(curr.left))
            rightMax = max(0, dfs(curr.right))
            currMax = max(leftMax,rightMax)

            self.res = max(self.res, leftMax + rightMax + curr.val)
        
            return currMax + curr.val
        
        dfs(root)
        return self.res