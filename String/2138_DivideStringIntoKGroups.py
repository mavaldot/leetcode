class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            group = ""
            j = 0
            while j < k and i+j < len(s):
                group += s[i+j]
                j += 1
            l = len(group)
            print(l)
            while (l < k):
                group += fill
                l += 1
                j += 1
            res.append(group) 
            i += j
        return res