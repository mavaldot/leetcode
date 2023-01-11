class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l+r)//2
        while (l <= r):
            mid = (l + r)//2
            print(mid)
            if nums[mid] > target:
                print(f"{nums[mid]} less")
                r = mid - 1
            elif nums[mid] < target:
                print(f"{nums[mid]} greater")
                l = mid + 1
            else:
                return mid
        return r + 1