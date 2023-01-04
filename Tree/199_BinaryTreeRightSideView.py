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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.explore(root, 0)
        res = []
        for lvl in self.levels:
            res.append(lvl[~0])
        return res