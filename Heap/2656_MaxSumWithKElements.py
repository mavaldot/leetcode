class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        hp = []
        score = 0
        for num in nums:
            heapq.heappush(hp, -num)
        
        for i in range(k):
            m = -heapq.heappop(hp)
            print(m)
            score += m
            heapq.heappush(hp, -(m+1))
            
        return score