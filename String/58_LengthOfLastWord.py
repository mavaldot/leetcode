class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        reached = False
        l = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if reached:
                    return l
            else:
                reached = True
                l += 1
        return l