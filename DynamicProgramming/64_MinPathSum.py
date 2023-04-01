class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        minPath = 0
        dp = [[float("inf")] * n for _ in range(m)]

        dp[-1][-1] = grid[-1][-1]

        for i in range(2, n+1):
            dp[-1][-i] = grid[-1][-i] + dp[-1][-i+1]
        for i in range(2, m+1):
            dp[-i][-1] = grid[-i][-1] + dp[-i+1][-1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])     
        print(grid)
        print(dp)

        return dp[0][0]