class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        j = 0
        n = len(nums)
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                k += 1
        
        return k
