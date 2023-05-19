class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        boomerangs = 0

        for i in range(len(points)):
            distPoint = defaultdict(int)
            # print(points[i])
            for j in range(len(points)):
                if i == j: continue
                x, y = points[i]
                x0, y0 = points[j]
                d = (x - x0)**2 + (y - y0)**2
                boomerangs += distPoint[d]
                distPoint[d] += 2
                # print(distPoint)
            # print("#####")

        return boomerangs