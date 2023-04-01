class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def combineHelper(rem, x, arr):
            if x > n: return
            if rem == 0:
                res.append(arr)
                return
            for i in range(x+1, n+1):
                arr.append(i)
                combineHelper(rem-1, i, arr[:])
                arr.pop()
        
        combineHelper(k, 0, [])
        return res