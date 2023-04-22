class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        maxPrime = 0
        
        def isPrime(n):
            if n == 1 or n == 0: return False
            if n == 2 or n == 3: return True
            for i in range(2, math.ceil(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        for i in range(len(nums)):
            if isPrime(nums[i][i]):
                maxPrime = max(maxPrime, nums[i][i])
            if isPrime(nums[i][~i]):
                maxPrime = max(maxPrime, nums[i][~i])
        
        return maxPrime