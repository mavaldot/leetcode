# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vals = []
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.visit(root, 1)
        for i in range(1, len(self.vals), 2):
            self.vals[i].reverse()
        return self.vals

    def visit(self, node, level):
        if node is None: return
        if len(self.vals) < level:
            self.vals.append([])
        self.vals[level-1].append(node.val)
        self.visit(node.left, level+1)
        self.visit(node.right, level+1)