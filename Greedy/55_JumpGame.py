class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        
        maxL = nums[0]

        for i in range(len(nums)):
            
            if maxL >= len(nums) - 1:
                return True

            if i > maxL:
                return False

            l = i + nums[i]
            maxL = max(l, maxL)
            
        return True