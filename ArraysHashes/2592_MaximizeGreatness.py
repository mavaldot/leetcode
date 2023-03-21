class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        greatness = 0
        dup = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                greatness += 1
            else:
                dup.append(nums[i-1])
                if dup[0] < nums[i]:
                    dup.pop(0)
                    greatness += 1
                
        return greatness