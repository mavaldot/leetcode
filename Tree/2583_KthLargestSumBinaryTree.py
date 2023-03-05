# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        self.sums = []
        
        def explore(node, level):
            if node is None: return
            
            if len(self.sums) < level:
                self.sums.append(0)
            
            self.sums[level-1] += node.val
            explore(node.left, level+1)
            explore(node.right, level+1)
            
        explore(root, 1)
        
        print(self.sums)
        
        self.sums.sort()
        
        if len(self.sums) < k: return -1
        
        return self.sums[-k]