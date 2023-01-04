# This solution is really hacky and inefficient, but it works! :)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.maxPath = float("-inf")

    def pathSum(self, node: Optional[TreeNode]) -> int:
        if node is None: return 0

        leftLeg = self.pathSum(node.left)
        rightLeg = self.pathSum(node.right)

        path = leftLeg + rightLeg + node.val
        path2 = node.val + max(leftLeg, rightLeg)
        path3 = node.val

        maxPoss = max(path2, path3)
        
        self.maxPath = max(self.maxPath, path)
        self.maxPath = max(self.maxPath, maxPoss)
        return maxPoss

    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum(root)
        return self.maxPath