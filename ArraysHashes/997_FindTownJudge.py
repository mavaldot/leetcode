class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        
        cand = set()
        elim = set()
        trustedBy = defaultdict(list)

        for a, b in trust:
            if b not in elim:
                cand.add(b)
            cand.discard(a)
            elim.add(a)
            trustedBy[b].append(a)

        for c in cand:
            if len(trustedBy[c]) == n - 1:
                return c
        
        return -1