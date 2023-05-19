class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        maxUnits = 0

        for num, units in boxTypes:
            for _ in range(num):
                heapq.heappush(heap, -units)
        
        while heap and truckSize:
            x = heapq.heappop(heap)
            maxUnits -= x    
            truckSize -= 1
        
        return maxUnits