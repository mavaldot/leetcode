# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.good = 1

    def goodNode(self, root: Optional[TreeNode], max: int):
        if root is None: return
        if max <= root.val:
            self.good += 1
            max = root.val
        self.goodNode(root.left, max)
        self.goodNode(root.right, max)

    def goodNodes(self, root: TreeNode) -> int:
        self.goodNode(root.left, root.val)
        self.goodNode(root.right, root.val)
        return self.good