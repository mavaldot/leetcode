class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        prev = [1] * len(nums)
        longest = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    # print(f"{nums[j]}, {nums[i]}")
                    # print(prev)
                    prev[i] = max(prev[i], prev[j] + 1)
                    longest = max(longest, prev[i])
        
        return longest