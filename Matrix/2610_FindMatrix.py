class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cn = defaultdict(int)
        res = []
        for n in nums:
            cn[n] += 1
            if cn[n] > len(res):
                res.append([])
            res[cn[n]-1].append(n)
        return res