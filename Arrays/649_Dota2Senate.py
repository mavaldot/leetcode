class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = inf
        r = inf
        n = len(senate)

        arr = list(senate)

        print(arr)
        skipD = 0
        skipR = 0

        while d > 0 and r > 0 and arr:
            newArr = []
            nd = 0
            nr = 0
            for s in arr:
                if s == 'D':
                    if skipD > 0:
                        skipD -= 1
                    else:
                        newArr.append('D')
                        nd += 1
                        skipR += 1
                else:
                    if skipR > 0:
                        skipR -= 1
                    else:
                        newArr.append('R')
                        nr += 1
                        skipD += 1
            arr = newArr
            d = nd
            r = nr

        return "Radiant" if arr[0] == 'R' else "Dire"    