# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.travel(root)
        return self.res

    def travel(self, node):
        if not node:
            return
        self.res.append(node.val)
        self.travel(node.left)
        self.travel(node.right)