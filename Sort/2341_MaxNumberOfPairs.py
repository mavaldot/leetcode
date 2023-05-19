class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        pairs = 0
        leftover = len(nums)
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                pairs += 1
                leftover -= 2
                i += 1
            i += 1

        return [pairs, leftover]