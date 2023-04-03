class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        minNums = [0] * len(spells)
        res = [0] * len(spells)
        m = {}
        potions.sort()

        for i in range(len(spells)):
            minNums[i] = math.ceil(success/spells[i])

        for i in range(len(minNums)):
            cnt = 0
            if minNums[i] in m:
                cnt = m[minNums[i]]
            else:
                cnt = len(potions) - bisect_left(potions, minNums[i])
                m[minNums[i]] = cnt
            res[i] = cnt
        return res