class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = 0
        ones = 0
        longest = 0
        
        for c in s:
            if c == "0":
                if ones > 0:
                    ones = 0
                    zeros = 0
                zeros += 1
            else:
                ones += 1
            if zeros >= ones:
                longest = max(longest, ones * 2)
        
        return longest