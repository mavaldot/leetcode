class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]

        cur = 1
        target = n * n

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        x, y = 0, 0

        while (cur <= target):
            m[x][y] = cur
            cur += 1
            dx = x + directions[d][0]
            dy = y + directions[d][1]
            if (dx < 0 or dx >= n or dy < 0 or dy >= n or m[dx][dy] > 0):
                d = (d + 1) % 4
                dx = x + directions[d][0]
                dy = y + directions[d][1]
            x, y = dx, dy

        return m