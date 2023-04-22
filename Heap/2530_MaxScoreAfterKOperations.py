class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = []
        score = 0

        for num in nums:
            heapq.heappush(hp, -num)
        
        for i in range(k):
            cur = -heapq.heappop(hp)
            score += cur
            heapq.heappush(hp, -math.ceil(cur/3))

        return score