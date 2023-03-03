class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        
        if len(nums) <= 3:
            return 0
        
        val1 = nums[~0] - nums[2]
        val2 = nums[~2] - nums[0]
        val3 = nums[~1] - nums[1]
        
        return min(val1, val2, val3)