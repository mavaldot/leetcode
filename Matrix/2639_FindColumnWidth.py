class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        for j in range(len(grid[0])):
            maxWidth = 0
            for i in range(len(grid)):
                n = grid[i][j]
                curWidth = 0 if n > 0 else 1
                n = abs(n)
                while n > 0:
                    n //= 10
                    # print(n)
                    curWidth += 1
                maxWidth = max(curWidth, maxWidth)
            res.append(maxWidth)
        return res