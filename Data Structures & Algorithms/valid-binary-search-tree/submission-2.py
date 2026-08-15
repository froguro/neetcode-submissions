# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(minVal, maxVal, curr):
            if not curr:
                return True
            if curr.val < maxVal and minVal < curr.val:
                return dfs(minVal,curr.val,curr.left) and dfs(curr.val, maxVal, curr.right)
            return False

        return dfs(float('-inf'), float('inf'), root)
        

            