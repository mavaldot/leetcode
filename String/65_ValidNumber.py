class Solution:
    def isNumber(self, s: str) -> bool:
        digits = set("0123456789")
        
        i = 0
        if s[i] == "+" or s[i] == "-":
            i += 1
        
        seenDigit = False
        seenDot = False
        seenE = False
        while (i < len(s)):
            if s[i] in digits:
                seenDigit = True
            elif s[i] == ".":
                if seenDot or seenE: return False
                seenDot = True
            elif s[i] == "e" or s[i] == "E":
                if seenE or not seenDigit: return False
                seenE = True
                seenDigit = False
                if i < len(s) - 1 and (s[i+1] == "+" or s[i+1] == "-"):
                    i += 1
            else:
                return False
            i += 1

        return seenDigit