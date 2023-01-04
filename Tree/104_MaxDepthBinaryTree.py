class Solution:
    def checkDepth(self, node: Optional[TreeNode], n: int) -> int:
        if node is None:
            return n
        else:
            left = self.checkDepth(node.left, n+1)
            right = self.checkDepth(node.right, n+1)
            return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.checkDepth(root, 0)