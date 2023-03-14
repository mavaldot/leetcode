class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxPath = 0
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def search(x, y, prev, visit):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or (x, y) in visit:
                return 0
            visit.add((x,y))
            if matrix[x][y] <= prev:
                return 0
            if dp[x][y] >= 0:
                return dp[x][y]
            val = matrix[x][y]
            u = 1 + search(x, y+1, val, visit.copy())
            d = 1 + search(x, y-1, val, visit.copy())
            l = 1 + search(x-1, y, val, visit.copy())
            r = 1 + search(x+1, y, val, visit.copy())
            largest = max(u, d, l, r)
            dp[x][y] = largest
            return largest
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visit = set()
                path = search(i, j, -1, visit)
                dp[i][j] = path
                maxPath = max(path, maxPath)
        print(dp)

        return maxPath