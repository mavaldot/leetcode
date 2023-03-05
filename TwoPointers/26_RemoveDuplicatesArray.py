class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        k = 1
        while (j < len(nums)):
            if nums[j] != nums[i]:
                i += 1
                k += 1
                nums[i] = nums[j]
            j += 1
        return k