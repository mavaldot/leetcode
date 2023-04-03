class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        k = 0
        count = 0
        prev = ""
        while (j < len(nums)):
            if nums[j] == prev:
                if count < 2:
                    count += 1
                    nums[i] = nums[j]
                    i += 1
                    k += 1
            else:
                prev = nums[j]
                count = 1
                nums[i] = nums[j]
                i += 1
                k += 1
            j += 1
        return k