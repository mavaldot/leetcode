class Solution:
    
    def invertChildren(self, node: Optional[TreeNode]) -> None:
        if node is None: return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.invertChildren(node.left)
        self.invertChildren(node.right)

    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertChildren(root)
        return root