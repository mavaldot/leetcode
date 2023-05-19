class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        mTravel, pTravel, gTravel = 0, 0, 0
        m, p, g = 0, 0, 0

        for l in garbage[0]:
            if l == "M":
                m += 1
            if l == "P":
                p += 1
            if l == "G":
                g += 1

        t = 0

        for i in range(1, len(garbage)):
            t += travel[i-1]
            
            for l in garbage[i]:
                if l == "M":
                    m += 1
                    mTravel = t
                if l == "P":
                    p += 1
                    pTravel = t
                if l == "G":
                    g += 1
                    gTravel = t
        
        return m + p + g + mTravel + pTravel + gTravel
