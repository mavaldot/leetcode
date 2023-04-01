class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        m = {}
        g = defaultdict(list)
        cycle = float("inf")
        
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(i, x):
            nonlocal cycle
            m[i] = x
            for neig in g[i]:
                if neig in m:
                    diff = x - m[neig]
                    if diff > 1:
                        cycle = min(diff+1, cycle)
                else:
                    dfs(neig, x+1)
        
        for num in range(n):
            m = {}
            dfs(num, 0)
        
        if cycle == float("inf"): return -1
        return cycle