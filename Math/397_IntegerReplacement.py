class Solution:
    def integerReplacement(self, n: int) -> int:

        ops = 0


        def operate(num, ops):
            if num == 1:
                return ops
            if num % 2 == 0:
                return operate(num//2, ops+1)
            else:
                return min(operate(num+1, ops+1), operate(num-1, ops+1))

        return operate(n, 0)