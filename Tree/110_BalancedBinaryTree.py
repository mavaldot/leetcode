class Solution:

    def checkBalance(self, node: Optional[TreeNode]):
        if node is None: return [True, 0]

        lbalance, lheight = self.checkBalance(node.left)
        rbalance, rheight = self.checkBalance(node.right)

        if not (lbalance and rbalance):
            return [False, -1]

        if abs(lheight - rheight) > 1:
            return [False, -1]

        return [True, 1 + max(lheight, rheight)]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.checkBalance(root)
        return balanced