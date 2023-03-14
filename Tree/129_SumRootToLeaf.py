class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        def helper(node, prev):
            if node is None: return
            prev = prev*10 + node.val
            if node.left is None and node.right is None:
                self.totalSum += prev
            helper(node.left, prev)
            helper(node.right, prev)
        helper(root, 0)
        return self.totalSum