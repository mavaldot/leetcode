class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        last = 0
        for i in range(0, x):
            if i * i > x:
                return last
            elif i * i == x:
                return i
            last = i
        return last