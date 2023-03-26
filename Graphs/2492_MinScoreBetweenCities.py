class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        score = float("inf")
        m = defaultdict(list)
        visit = set()
        q = []
        for a, b, dist in roads:
            m[a].append((b, dist))
            m[b].append((a, dist))
        
        for b, dist in m[1]:
            visit.add(1)
            q.append((b, dist))
        
        while (q):
            b, dist = q.pop()
            if b not in visit:
                visit.add(b)
                for c, d in m[b]:
                    q.append((c, d))
            score = min(score, dist)

        return score