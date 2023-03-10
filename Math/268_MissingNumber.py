class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = n * (n + 1) / 2
        total = sum(nums)
        res = int(s - total)
        return res