# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.levels = []
    
    def explore(self, node: Optional[TreeNode], lvl: int):
        if node is None: return
        if len(self.levels) < lvl + 1:
            self.levels.append([])
        self.levels[lvl].append(node.val)
        nextLvl = lvl + 1
        self.explore(node.left, nextLvl)
        self.explore(node.right, nextLvl)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.explore(root, 0)
        return self.levels