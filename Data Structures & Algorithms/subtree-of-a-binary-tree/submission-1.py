class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # Check if subtree starts at current root OR exists in left/right subtrees
        return (self.isSameTree(root, subRoot) or 
                self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
