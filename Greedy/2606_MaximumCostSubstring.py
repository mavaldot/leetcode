class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        alphabet = string.ascii_lowercase
        m = {}
        for i, c in enumerate(alphabet):
            m[c] = i + 1
        
        for i in range(len(chars)):
            m[chars[i]] = vals[i]
        
        sm = 0
        res = 0
        
        for c in s:
            sm += m[c]
            res = max(res, sm)
            if sm < 0: sm = 0
        
        return res