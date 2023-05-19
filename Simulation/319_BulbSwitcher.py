class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulb = 0
        i = 1
        while i * i <= n:
            bulb += 1
            i += 1
        return bulb