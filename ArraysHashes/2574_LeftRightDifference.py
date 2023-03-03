class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        leftSum = 0
        rightSum = 0
        for j in range(0, len(nums)):
            rightSum += nums[j]
        print(res)
        for i in range(len(nums)):
            print(f"leftsum: {leftSum}, rightsum: {rightSum}")
            rightSum -= nums[i]
            res[i] = abs(leftSum - rightSum)
            leftSum += nums[i]
            
            
        return res