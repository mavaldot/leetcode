class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        consec = 0
        for num in nums:
            if num == 0:
                consec += 1
            else:
                if consec > 0:
                    res += consec * (consec+1) // 2
                    consec = 0
        res += consec * (consec+1) // 2
        return res