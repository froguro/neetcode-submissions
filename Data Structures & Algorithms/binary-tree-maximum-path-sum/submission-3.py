# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def recurse(curr):
            if not curr:
                return 0
            leftMax = max(0, recurse(curr.left))
            rightMax = max(0, recurse(curr.right))

            currMax = leftMax + rightMax + curr.val
            self.res = max(self.res, currMax)

            return curr.val + max(leftMax, rightMax)
        
        recurse(root)
        return self.res

