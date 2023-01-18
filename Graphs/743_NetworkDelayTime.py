
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTimes = [0] * n
        visit = set()

        adj = defaultdict(list)

        minHp = [] 

        for u, v, w in times:
            adj[u].append((v, w))
            
        heapq.heappush(minHp, (0, k))
        while (minHp):
            (w, v) = heapq.heappop(minHp)
            if v in visit: continue
            print(f"after pop: {v}, {w} ")
            minTimes[v-1] = w
            visit.add(v)
            for vv, ww in adj[v]:
                if vv not in visit:
                    print(f"{vv}, {ww}")
                    heapq.heappush(minHp, (w + ww, vv))

        print(len(visit))

        print(minTimes)

        if len(visit) != n:
            return -1

        return max(minTimes)