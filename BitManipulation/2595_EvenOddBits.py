class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        while n:
            if (n & 1): even += 1
            n >>= 1
            if (n & 1): odd += 1
            n >>= 1
        return [even, odd]