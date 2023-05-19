class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        n = len(derived)

        original0 = [0] * n
        original1 = [1] * n

        for i in range(n-1):
            if derived[i] == 1:
                original0[i+1] = not original0[i]
                original1[i+1] = not original1[i]
            else:
                original0[i+1] = original0[i]
                original1[i+1] = original1[i]

        if original0[n-1] ^ original0[0] == derived[n-1]: return True
        if original1[n-1] ^ original1[0] == derived[n-1]: return True

        return False
