class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        moves = 0
        
        while (maxDoubles > 0):
            if target <= 2: break
            if target % 2 == 0:
                target = target//2
                maxDoubles -= 1
                moves += 1
            else:
                target -= 1
                moves += 1
        
        return moves + target - 1