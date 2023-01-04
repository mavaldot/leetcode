class Solution:
    
    def checkSame(self, p, q):
        if not (p or q):
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        left_check = self.checkSame(p.left, q.left)
        right_check = self.checkSame(p.right, q.right)

        return left_check and right_check
        
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.checkSame(p, q)