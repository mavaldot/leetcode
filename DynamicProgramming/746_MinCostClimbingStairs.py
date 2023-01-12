class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def climb(n):
            if n <= 1: return 0

            return min(climb(n-2)+cost[n-2], climb(n-1)+cost[n-1])
        return climb(len(cost))