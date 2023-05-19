class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        dup = set()
        idx = deque()

        for i, c in enumerate(s):
            # print(idx)
            if c in seen:
                dup.add(c)
            else:
                seen.add(c)
                idx.append(i)
            while idx and s[idx[0]] in dup:
                idx.popleft()
        
        return idx[0] if idx else -1