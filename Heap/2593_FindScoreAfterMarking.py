class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        seen = set()
        places = defaultdict(list)
        hp = []
        score = 0
        for i, num in enumerate(nums):
            heapq.heappush(hp, num)
            places[num].append(i)
        
        while (hp):
            cur = heapq.heappop(hp)
            if cur in seen: continue
            seen.add(cur)
            l = places[cur]
            for item in l:
                if item in marked: continue
                score += cur
                marked.add(item)
                marked.add(item-1)
                marked.add(item+1)
        
        return score