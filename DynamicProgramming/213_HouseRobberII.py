class Solution:
    def rob(self, nums: List[int]) -> int:

        sz = len(nums)

        if sz == 1: return nums[0]

        @cache
        def visitHouse(n):
            if n < 0:
                return 0
            return max(visitHouse(n-2)+nums[n], visitHouse(n-1))

        @cache
        def visitHouseMod(n):
            if n <= 0:
                return 0
            return max(visitHouseMod(n-2)+nums[n], visitHouseMod(n-1))

        return max(visitHouse(sz-2), visitHouseMod(sz-1)) 