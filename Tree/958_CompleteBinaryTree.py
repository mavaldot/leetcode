class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        self.arr = []

        def helper(node, level):
            if len(self.arr) < level:
                self.arr.append([])
            if node is None:
                self.arr[level-1].append(0)
                return
            self.arr[level-1].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 1)

        print(self.arr)

        foundZero = False
        for item in self.arr:
            for x in item:
                if x == 0:
                    foundZero = True
                else:
                    if foundZero: return False

        return True