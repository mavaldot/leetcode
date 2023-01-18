import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        q = []

        visit = set()
        heapq.heappush(q, (grid[0][0], 0, 0))
        leastTime = 0

        n = len(grid)
        m = len(grid[0])

        while (q):
            val, i, j = heapq.heappop(q)
            if (i,j) in visit: continue

            visit.add((i,j))
            leastTime = max(leastTime, val)

            if i == n - 1 and j == m - 1:
                return leastTime

            locs = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
            for dx, dy in locs:
                if dx >= 0 and dy >= 0 and dx < n and dy < m and (dx, dy) not in visit:
                    heapq.heappush(q, (grid[dx][dy],dx,dy))


        return leastTime