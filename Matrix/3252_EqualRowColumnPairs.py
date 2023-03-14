class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        n = len(grid)
        rows = {}
        for i in range(n):
            s = ""
            for j in range(n):
                s += f"#{grid[i][j]}"
            if s in rows:
                rows[s] += 1
            else:
                rows[s] = 1

        for i in range(n):
            s = ""
            for j in range(n):
                s += f"#{grid[j][i]}"
            if s in rows:
                pairs += rows[s]

        print(rows)
        return pairs