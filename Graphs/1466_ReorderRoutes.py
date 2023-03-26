class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visit = set()
        entering = defaultdict(list)
        exiting = defaultdict(list)
        reorder = 0

        for a, b in connections:
            entering[b].append(a)
            exiting[a].append(b)
        
        dq = deque([0])

        while (dq):
            cur = dq.popleft()
            if cur in visit: continue
            visit.add(cur)
            for item in entering[cur]:
                if item not in visit:
                    dq.append(item)
            for item in exiting[cur]:
                if item not in visit:
                    dq.append(item)
                    reorder += 1

        return reorder