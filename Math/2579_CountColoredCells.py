class Solution:
    def coloredCells(self, n: int) -> int:
        
        total = 0
        
        for i in range(1, n):
            total += (i*2-1)*2
        
        total += n*2-1
        
        return total