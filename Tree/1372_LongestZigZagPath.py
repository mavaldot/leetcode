class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.longest = 0

        def search(node, goLeft, val):
            if node is None:
                self.longest = max(val, self.longest)
                return
            elif goLeft:
                search(node.left, False, val+1)
                search(node.right, True, 0)
            else:
                search(node.right, True, val+1)
                search(node.left, False, 0)
        
        search(root.right, True, 0)
        search(root.left, False, 0)

        return self.longest