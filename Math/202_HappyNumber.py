class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def helper(n):
            if n == 1: return True
            temp = n
            prod = 0
            while (n > 0):
                digit = n % 10
                prod += digit**2
                n //= 10
            if prod in seen: return False
            seen.add(prod)
            return helper(prod)
        
        return helper(n)