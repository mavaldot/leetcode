class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        self.visit = set()
        self.perimeter = 0

        def navigate(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                self.perimeter += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    navigate(i+1, j)
                    navigate(i-1, j)
                    navigate(i, j+1)
                    navigate(i, j-1)

        return self.perimeter