class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        s = str(n)
        sign = 1
        
        
        for i in range(0, len(s)):
            res += int(s[i])*sign
            sign *= -1
        
        return res