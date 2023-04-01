class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def sieve():
            n = 1001
            isPrime = [True] * n
            isPrime[1] = False
            i = 2
            for i in range(2, n):
                for j in range(i*2, n, i):
                    isPrime[j] = False
            return isPrime

        primes = sieve()
        prev = -1

        for num in nums:
            found = False
            cur = float("-inf")
            for i in range(num-1, -1, -1):
                if primes[i] and num - i > prev:
                    cur = num - i
                    found = True
                    break
            if cur < prev: return False
            prev = cur

        return True
