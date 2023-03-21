class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        
        l = len(grid)
        dic = {}
        
        def check(n, i, j):
            if (i < 0 or i >= l or j < 0 or j >= l):
                return False
            if grid[i][j] == n:
                dic[n] = (i, j)
                return True
            return False
        
        squares = l * l
        x, y = 0, 0
        
        for k in range(1, squares):
            if not (check(k, x+2, y+1) or check(k, x+1, y+2)
                    or check(k, x+2, y-1) or check(k, x+1, y-2) 
                    or check(k, x-2, y+1) or check(k, x-2, y-1)
                    or check(k, x-1, y+2) or check(k, x-1, y-2)):
                print(f"{k} {x} {y}")
                return False
            x, y = dic[k]
        return True