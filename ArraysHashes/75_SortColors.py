class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for num in nums:
            if num == 0: r += 1
            elif num == 1: w += 1
            else: b += 1
        i = 0
        while r:
            nums[i] = 0
            r -= 1
            i += 1
        while w:
            nums[i] = 1
            w -= 1
            i += 1
        while b:
            nums[i] = 2
            b -= 1
            i += 1