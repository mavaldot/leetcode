# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minVal = float("inf")

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.difference(root, [])
        return self.minVal
    
    def difference(self, node, arr):
        arr.append(node.val)
        if node.left:
            for item in arr:
                valDiff = abs(item - node.left.val)
                self.minVal = min(valDiff, self.minVal)
            self.difference(node.left, arr[:])
        if node.right:
            for item in arr:
                valDiff = abs(item - node.right.val)
                self.minVal = min(valDiff, self.minVal)
            self.difference(node.right, arr[:])