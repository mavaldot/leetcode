class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        minDiff = inf
        res = 0
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while (j < k):
                sm = nums[i] + nums[j] + nums[k]
                diff = abs(target - sm)
                if diff < minDiff:
                    res = sm
                    minDiff = diff
                if sm < target:
                    j += 1
                elif sm == target:
                    break
                else:
                    k -= 1
            if minDiff == 0: break
        return res 