class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        
        if s == target: return True
        
        prevOne = False
        prevZero = False
        
        for i in range(len(s)):
            if s[i] == '1' and target[i] == '1':
                return True
            elif s[i] == '1':
                prevOne = True
            elif s[i] == '0' and target[i] == '1':
                prevZero = True
            
        return prevOne and prevZero