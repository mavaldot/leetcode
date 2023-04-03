class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        hp = []
        res = sum(reward2)
        
        diff = [0] * len(reward1)
        
        for i in range(len(reward1)):
            heapq.heappush(hp, [-(reward1[i] - reward2[i]), i])
        
        
        for i in range(k):
            a, b = heapq.heappop(hp)
            res += reward1[b]
            res -= reward2[b]
        
        return res