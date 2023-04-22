class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        chosen = 0
        sm = 0
        bannedSet = set(banned)
        for i in range(1, n+1):
            if i not in bannedSet:
                sm += i
                if sm > maxSum:
                    return chosen
                chosen += 1
        
        return chosen