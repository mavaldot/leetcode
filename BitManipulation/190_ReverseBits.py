class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(31):
            res += (n & 1)
            n >>= 1
            res <<= 1
        res += (n & 1)
        return res