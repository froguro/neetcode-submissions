# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(curr):
            if not curr:
                return "null,"
            return f"{curr.val}" + "," + preorder(curr.left) + preorder(curr.right) 

        return preorder(root)[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build():
            val = next(vals)
            if val == "null":
                return None
            root = TreeNode(int(val))
            root.left = build()
            root.right = build()
            return root
        
        vals = iter(data.split(","))
        return build()

