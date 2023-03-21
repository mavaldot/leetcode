class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0: return prefix
        i = 0
        common = True
        while (common):
            pre = ""
            if i >= len(strs[0]):
                return prefix
            else:
                pre = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != pre:
                    common = False
                    break
            i += 1
            if common: prefix += pre
                
        return prefix