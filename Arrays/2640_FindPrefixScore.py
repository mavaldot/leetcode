class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        mx = 0
        total = 0
        
        for i in range(n):
            mx = max(mx, nums[i])
            cur = nums[i] + mx
            total += cur
            res[i] = total
        
        return res
        