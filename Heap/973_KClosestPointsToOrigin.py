class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        indices = defaultdict(list)
        sizes = []
        res = []
        heapq.heapify(sizes)
        for i in range(0, len(points)):
            dist = points[i][0]**2 + points[i][1]**2
            heapq.heappush(sizes, dist)
            indices[dist].append(i)
        
        for j in range(0, k):
            d = heapq.heappop(sizes)
            print(d)
            index = indices[d].pop()
            res.append(points[index])

        return res