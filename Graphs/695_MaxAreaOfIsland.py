class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        self.curArea = 0
        self.maxArea = 0
        m = len(grid[0])
        n = len(grid)

        def dfs(i, j):
            if (i, j) in seen:
                return
            if i < 0 or j < 0 or i >= n or j >= m:
                return 
            if grid[i][j] == 0:
                return
            seen.add((i,j))
            self.curArea += 1
            self.maxArea = max(self.maxArea, self.curArea)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


        dfs(0, 0)

        for i in range(0, n):
            for j in range(0, m):
                self.curArea = 0
                dfs(i, j)

        return self.maxArea