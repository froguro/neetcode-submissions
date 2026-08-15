class Codec:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null,"
            return str(node.val) + "," + preorder(node.left) + preorder(node.right)
        
        return preorder(root)[:-1]  # Remove trailing comma
    
    def deserialize(self, data):
        def build():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        vals = iter(data.split(","))
        return build()
