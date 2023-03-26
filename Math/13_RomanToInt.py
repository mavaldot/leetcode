class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        cur = 0
        res = 0


        for c in s:
            prev = cur
            if c == "I":
                cur = 1
            elif c == "V":
                cur = 5
            elif c == "X":
                cur = 10
            elif c == "L":
                cur = 50
            elif c == "C":
                cur = 100
            elif c == "D":
                cur = 500
            elif c == "M":
                cur = 1000
            if prev < cur:
                cur -= prev * 2
            print(cur)
            res += cur
        
        return res