class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts = 0
        
        start = 0
        end = -1

        res = []

        for i in range(len(s)):
            last = i
            for j in range(len(s)):
                if s[j] == s[i]:
                    last = j
            end = max(last, end)
            if i == end:
                res.append(end-start+1)
                start = i + 1

        return res