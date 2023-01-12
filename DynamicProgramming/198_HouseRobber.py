class Solution:

    def rob(self, nums: List[int]) -> int:

        @cache
        def visitHouse(n):
            if n < 0:
                return 0
            if n == 0:
                return nums[0]
            return max(visitHouse(n-2)+nums[n], visitHouse(n-1))

        return visitHouse(len(nums)-1) 