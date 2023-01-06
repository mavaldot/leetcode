import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [item * -1 for item in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                print(y-x)
                heapq.heappush(stones, -(y-x))

        if stones:
            res = heapq.heappop(stones)
            return abs(res)
        return 0