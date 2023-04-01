class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        i = 0
        while (i < n and satisfaction[i] < 0):
            i += 1
        
        prev = 0
        time = 1
        for x in range(i, n):
            # print(f"{i}, {n}, {x}, {cur}, {satisfaction[x]}")
            prev += (time * satisfaction[x])
            time += 1
        
        for x in range(i-1, -1, -1):
            time = 1
            cur = 0
            for j in range(x, n):
                cur += (time * satisfaction[j])
                time += 1

            prev = max(cur, prev)

        return prev 