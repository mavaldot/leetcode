class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            return helper(n1.left, n2.right) and helper(n1.right, n2.left)
        
        return helper(root.left, root.right)