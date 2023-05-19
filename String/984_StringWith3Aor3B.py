class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ""
        while a > b:
            if a >= 2:
                s += "aa"
                a -= 2
                if b >= 1:
                    s += "b"
                    b -= 1
            else:
                s += "a"
                a -= 1
                if b >= 1:
                    s += "b"
                    b -= 1

        
        while b > a:
            if b >= 2:
                s += "bb"
                b -= 2
                if a >= 1:
                    s += "a"
                    a -= 1
            else:
                s += "b"
                b -= 1
                if a >= 1:
                    s += "a"
                    a -= 1
        
        while a > 0:
            s += "a"
            a -= 1
            if b:
                s += "b"
                b -= 1
        
        while b > 0:
            s += "b"
            b -= 1
        
        return s