# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            qLen = len(queue)
            currNode = None
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    currNode = node

            if currNode:
                print(currNode.val)
                res.append(currNode.val)
        
        return res