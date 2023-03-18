class Solution:
    def maxScore(self, nums: List[int]) -> int:
        prefixSum = 0
        nums.sort()
        nums = nums[::-1]
        x = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum <= 0:
                return x
            x += 1

        return x 